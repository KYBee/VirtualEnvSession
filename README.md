# VirtualEnvSession
피로그래밍 16기 Django개론 및 가상환경 세션 레퍼지토리

2. install package with .gitignore
- .gitignore을 잘 작성해서 venv가 업로드 되지 않음.
- Django를 설치하고 requirements.txt를 만듬

3. start django project
- django-admin startproject pirogramming16 명령어 실행
- pirogramming16이라는 장고 프로젝트 생성됨

4. make index page
- pirogramming16 디렉토리의 urls.py에서 index 요청을 매핑함
- views.py 를 만들고 index 요청에 대해 어떻게 대처할지 명시함
- pirogramming16 디렉토리(manage.py)가 있는 디렉토리에서 python manage.py runserver 실행 후, 127.0.0.1:8000 에 접근하면 우리가 정의한 index 페이지가 나오는 것을 확인할 수 있음