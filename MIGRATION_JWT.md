# JWT Library Migration: python-jose → PyJWT

## Background

**Date**: 2026-02-12  
**Issue**: The `ecdsa==0.19.1` package (dependency of `python-jose`) has a Minerva timing attack vulnerability with no patch available.

## Changes Made

### 1. Dependency Changes
**Removed**:
- `python-jose==3.5.0`
- `ecdsa==0.19.1` (transitive dependency)
- `pyasn1==0.6.2` (transitive dependency)
- `rsa==4.9.1` (transitive dependency)
- `six==1.17.0` (transitive dependency)

**Added**:
- `PyJWT==2.10.1` (actively maintained, no ecdsa dependency)

### 2. Code Changes
**File**: `backend/utils/auth.py`

**Before**:
```python
from jose import jwt, JWTError

# Usage
try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
except JWTError:
    # handle error
```

**After**:
```python
import jwt  # PyJWT
from jwt.exceptions import PyJWTError

# Usage (identical API)
try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
except PyJWTError:
    # handle error
```

## API Compatibility

✅ **100% Compatible**: PyJWT uses the same `jwt.encode()` and `jwt.decode()` API as python-jose.

The only changes required:
1. Import change: `from jose import jwt` → `import jwt`
2. Exception change: `JWTError` → `PyJWTError`

## Testing

### Verified Functionality
- ✅ JWT token creation (access & refresh tokens)
- ✅ JWT token verification
- ✅ JWT token expiration
- ✅ User authentication flow
- ✅ OAuth callback token generation

### Security Verification
- ✅ No vulnerabilities in PyJWT==2.10.1 (GitHub Advisory Database)
- ✅ HMAC-SHA256 (HS256) algorithm still used
- ✅ Token lifetime unchanged (30 minutes for access, 30 days for refresh)
- ✅ All Python files compile successfully

## Impact Assessment

### Zero Functional Impact
- ✅ No breaking changes to API
- ✅ No changes to token format
- ✅ Existing tokens will continue to work
- ✅ No database changes required
- ✅ No frontend changes required

### Security Improvement
- ✅ Removed vulnerable ecdsa dependency
- ✅ Using more actively maintained library (PyJWT)
- ✅ Smaller dependency tree (5 fewer packages)

## Migration Steps (For Existing Deployments)

If you're running LifeAdmin in production:

### 1. Update Dependencies
```bash
cd backend
pip uninstall python-jose ecdsa pyasn1 rsa six -y
pip install PyJWT==2.10.1
```

Or simply:
```bash
pip install -r requirements.txt
```

### 2. Restart Application
```bash
# No database migrations needed
# No cache clearing needed
# Just restart the server
uvicorn main:app --reload
```

### 3. Verify
```bash
# Test login endpoint
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password"}'

# Should return access_token and refresh_token as before
```

## Rollback Plan

If any issues arise (unlikely):

1. Revert `backend/utils/auth.py` to previous version
2. Reinstall old dependencies:
   ```bash
   pip uninstall PyJWT -y
   pip install python-jose==3.5.0
   ```
3. Restart server

## Why PyJWT?

1. **Active Maintenance**: PyJWT is actively maintained by the PyJWT team
2. **No ECDSA**: Doesn't depend on the vulnerable ecdsa package
3. **Better Performance**: Lighter weight, fewer dependencies
4. **Same API**: Drop-in replacement for python-jose
5. **Better Documentation**: More comprehensive docs and examples
6. **More Popular**: 6.5k+ GitHub stars vs python-jose's 1.5k

## References

- [PyJWT Documentation](https://pyjwt.readthedocs.io/)
- [ecdsa Minerva Vulnerability](https://github.com/advisories/GHSA-wj6h-64fc-37mp)
- [python-jose GitHub](https://github.com/mpdavis/python-jose)
- [PyJWT GitHub](https://github.com/jpadilla/pyjwt)

## Questions?

If you have questions about this migration, please open a GitHub issue.

---

**Status**: ✅ Complete  
**Testing**: ✅ Passed  
**Security Scan**: ✅ Clean  
**Rollback Risk**: Low  
**Recommended Action**: Deploy immediately
