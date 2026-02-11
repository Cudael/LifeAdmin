from fastapi import HTTPException, UploadFile
import os
import magic  # Install: pip install python-magic
import logging

logger = logging.getLogger(__name__)

# Allowed file types
ALLOWED_EXTENSIONS = {
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
    'jpg', 'jpeg', 'png', 'gif', 'webp',
    'txt', 'csv', 'zip', 'rar'
}

ALLOWED_MIME_TYPES = {
    'application/pdf',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'image/jpeg',
    'image/png',
    'image/gif',
    'image/webp',
    'text/plain',
    'text/csv',
    'application/zip',
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def validate_file(file: UploadFile) -> tuple[bool, str]:
    """
    Validate uploaded file
    Returns: (is_valid, error_message)
    """
    if not file or not file.filename:
        return True, ""  # No file uploaded is okay
    
    # Check file extension
    file_ext = file.filename.rsplit('.', 1)[-1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        logger.warning(f"Blocked file upload with extension: {file_ext}")
        return False, f"File type .{file_ext} is not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
    
    # Check file size
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to start
    
    if file_size > MAX_FILE_SIZE:
        logger.warning(f"Blocked file upload exceeding size limit: {file_size} bytes")
        return False, f"File size ({file_size / 1024 / 1024:.2f}MB) exceeds limit of 10MB"
    
    if file_size == 0:
        return False, "File is empty"
    
    # Check MIME type (if python-magic is available)
    try:
        file_content = file.file.read(2048)  # Read first 2KB
        file.file.seek(0)  # Reset
        
        mime = magic.from_buffer(file_content, mime=True)
        
        if mime not in ALLOWED_MIME_TYPES:
            logger.warning(f"Blocked file upload with MIME type: {mime}")
            return False, f"File type {mime} is not allowed"
    except Exception as e:
        logger.warning(f"Could not validate MIME type: {e}")
        # Continue without MIME validation if library not available
    
    return True, ""


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename to prevent directory traversal
    """
    # Remove path separators
    filename = os.path.basename(filename)
    
    # Remove dangerous characters
    dangerous_chars = ['..', '/', '\\', '<', '>', ':', '"', '|', '?', '*']
    for char in dangerous_chars:
        filename = filename.replace(char, '_')
    
    # Limit length
    name, ext = os.path.splitext(filename)
    if len(name) > 100:
        name = name[:100]
    
    return f"{name}{ext}"