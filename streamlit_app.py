import streamlit as st
import pypdf
import io # Used to handle files in memory

# --- Page Configuration ---
st.set_page_config(
    page_title="PDF Password Remover",
    page_icon="🔓",
    layout="centered"
)

# --- App UI and Logic ---
st.title("🔓 PDF Password Remover")
st.markdown("Upload your password-protected PDF files, and this tool will help you remove the password.")

# 1. File Uploader
uploaded_files = st.file_uploader(
    "Choose one or more PDF files",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:
    st.info(f"You have uploaded {len(uploaded_files)} file(s).")
    
    for uploaded_file in uploaded_files:
        st.markdown("---")
        st.write(f"**Processing:** `{uploaded_file.name}`")

        try:
            # Create a reader object from the uploaded file's bytes
            # We use BytesIO to treat the uploaded file's bytes like a file on disk
            file_bytes = io.BytesIO(uploaded_file.getvalue())
            reader = pypdf.PdfReader(file_bytes)
            
            # 2. Check for Encryption and Ask for Password
            if reader.is_encrypted:
                # Use a unique key for each password field to avoid conflicts
                password = st.text_input(
                    f"Enter password for `{uploaded_file.name}`", 
                    type="password", 
                    key=f"password_{uploaded_file.name}"
                )
                
                if not password:
                    st.warning("Please enter the password to proceed.")
                    # Skip to the next file if no password is provided for this one
                    st.stop() 

                if reader.decrypt(password):
                    st.success("Password accepted!")
                else:
                    st.error("Incorrect password. Please try again.")
                    # Skip to the next file if password is wrong
                    st.stop() 
            else:
                st.write("This PDF is not password protected.")

            # 3. Create a New Unprotected PDF in Memory
            writer = pypdf.PdfWriter()
            for page in reader.pages:
                writer.add_page(page)

            # Save the new PDF to a BytesIO object in memory
            output_pdf_bytes = io.BytesIO()
            writer.write(output_pdf_bytes)
            # Reset the "cursor" to the beginning of the byte stream
            output_pdf_bytes.seek(0)

            # 4. Provide a Download Button
            st.download_button(
                label=f"Download Unlocked '{uploaded_file.name}'",
                data=output_pdf_bytes,
                file_name=f"unlocked_{uploaded_file.name}",
                mime="application/pdf",
                key=f"download_{uploaded_file.name}"
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")