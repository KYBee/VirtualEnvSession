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

5. make hello app
- app은 장고 프로젝트의 하나의 기능이라고 생각하면 됨. 인사를 하는 기능을 가진 hello app을 만듬
- app을 만든 뒤에 프로젝트의 settings.py 파일의 INSTALLED_APP 에 만든 앱을 등록함

6. make hello page
- 프로젝트 디렉토리의 urls.py 에 hello url pattern 등록 : 이제부터 127.0.0.1:8000/hello로 들어오는 url을 처리할 수 있음
- hello app 디렉토리에 urls.py 생성
- hello app 디렉토리의 views.py 에 hello로 들어오는 요청을 다루기 위한 코드 작성
- hello 라는 요청이 온다면 장고의 View는 Template hello.html을 부르도록 코드 작성
- hello app 디렉토리의 template 안에 있는 hello.html을 작성하여 사용자에게 어떻게 보여줄지를 작성
- 127.0.0.1:8000/hello로 접속할 경우에 작성한 html이 보이는 것을 확인할 수 있음