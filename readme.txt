UGHE Test Web App — Backend (readme.txt)
=========================================

GitHub repositories (public):
  Backend (this repo):  https://github.com/ndahiroloicke/ughe-test-backend
  Frontend (Next.js):   https://github.com/ndahiroloicke/ughe-test-frontend

HOW TO RUN THIS REPO ALONE (Docker)
------------------------------------
1. Clone: git clone https://github.com/ndahiroloicke/ughe-test-backend.git
2. cd ughe-test-backend
3. docker compose up --build
4. Wait until Gunicorn is listening.
5. Verify: http://localhost:8000/api/homepage/
6. Admin:  http://localhost:8000/admin/
   User: ughe_admin  Password: UGHE_Test_2024!

Stop: docker compose down

Then start the frontend repo (see ughe-test-frontend readme) on port 3000.

Optional local Python setup: see README.md

Libraries: requirements.txt
