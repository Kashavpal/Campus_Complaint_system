import os, uuid
from functools import wraps
from flask import session, redirect, url_for, flash
from PIL import Image
ALLOWED_IMAGES={'jpg','jpeg','png','webp'}; ALLOWED_ATTACHMENTS=ALLOWED_IMAGES|{'pdf'}
def login_required(view):
    @wraps(view)
    def wrapper(*a,**k):
        if 'user_id' not in session: flash('Please log in.','warning'); return redirect(url_for('login'))
        return view(*a,**k)
    return wrapper
def role_required(*roles):
    def deco(view):
        @wraps(view)
        def wrapper(*a,**k):
            if 'user_id' not in session: return redirect(url_for('login'))
            if session.get('role') not in roles: flash('Not authorized.','danger'); return redirect(url_for('dashboard'))
            return view(*a,**k)
        return wrapper
    return deco
def safe_image_save(fs,d):
    if not fs or not fs.filename: raise ValueError('Image is required.')
    ext=fs.filename.rsplit('.',1)[-1].lower() if '.' in fs.filename else ''
    if ext not in ALLOWED_IMAGES: raise ValueError('Only JPG, JPEG, PNG and WEBP images are allowed.')
    os.makedirs(d,exist_ok=True); name=f'{uuid.uuid4().hex}.{ext}'; path=os.path.join(d,name); fs.save(path)
    try:
        with Image.open(path) as im: im.verify()
    except Exception:
        try: os.remove(path)
        except OSError: pass
        raise ValueError('Invalid image.')
    return name
def safe_attachment_save(fs,d):
    if not fs or not fs.filename: return None
    ext=fs.filename.rsplit('.',1)[-1].lower() if '.' in fs.filename else ''
    if ext not in ALLOWED_ATTACHMENTS: raise ValueError('Attachment type is not allowed.')
    os.makedirs(d,exist_ok=True); name=f'{uuid.uuid4().hex}.{ext}'; fs.save(os.path.join(d,name)); return name
def delete_file(path):
    if path and os.path.exists(path):
        try: os.remove(path)
        except OSError: pass
