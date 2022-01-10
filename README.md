# VirtualEnvSession
피로그래밍 16기 Django개론 및 가상환경 세션 레퍼지토리

1. install_package
- .gitignore을 작성하지 않아서 venv가 올라간 상황
- 이런 상황을 방지하기 위해서 .gitignore을 작성해야 함
- 이렇게 하면 안된다는 것을 알려드리기 위해 임시적으로 만든 브랜치. 해당 브랜치에 들어가보면 venv가 레퍼지토리에 업로드 되어 있는 것을 볼 수 있음

2. install package with .gitignore
- .gitignore을 잘 작성해서 venv가 업로드 되지 않음
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



위의 브랜치를 클릭하시면 번호에 맞게 조취가 취해진 브랜치들이 만들어져 있습니다.
연습을 진행하다가 막히는 부분이 있거나 동작하지 않는 경우에는 각 브랜치에 들어가셔서 무엇이 다른지 찾아보시면 좋습니다.

화이팅!