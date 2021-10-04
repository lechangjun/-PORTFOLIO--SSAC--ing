# 프로젝트를 위한 공부 자료



## kubeflow_k8s 정리
### kubeflow 란
Kubeflow는 Kubernetes + ML flow를 합한 의미로, 파이프라인이라는 ML워크플로를 구축하고 배포하기 위해 제공되는 플랫폼입니다
### 파이프라인 구성 요소 이해
[![image](https://user-images.githubusercontent.com/68671394/135787947-4e5a22ad-ef3d-4f67-863c-38f15b9d12eb.png)](https://www.kubeflow.org/docs/components/notebooks/)


AI HUB의 파이프라인 워크플로우는 데이터 사전 처리, 데이터 변환, 모델 학습 등과 같은 단계로 구성되어 있습니다. 워크플로우의 구성요소는 입력 매개 변수 세트, 출력 세트 및 컨테이너 이미지의 위치로 구성되어 있습니다. 구성요소의 컨테이너 이미지는 구성 요소의 실행 코드와 코드가 실행되는 환경의 정의를 포함하는 패키지로 이루어져있습니다.
### kubeflow 개념적 개요
- Kubeflow는 쿠버네티스에서 머신 러닝 워크 플로를 실행하기 위해서 만들어졌습니다. 일반적으로 다음과 같은 이유로 사용할 수 있습니다.
- 이미 쿠버네티스 기반의 인프라가 있거나, 새로운 머신 러닝 플랫폼을 만들려는 경우
- 다양한 환경(예 : 로컬, 온 프레미스 및 클라우드)에서 머신 러닝 모델을 학습하거나 서비스하려는 경우
- 자원(예 : CPU 또는 GPU)를 할당하여 작업을 하려는 경우
- Jupyter 노트북을 사용하여 머신 러닝 작업을 하려는 경우
- Kubeflow에는 Jupyter 노트북 생성 및 관리를 위한 서비스를 이용할 때
- Kubeflow Pipelines는 Docker 컨테이너를 기반으로하는 다단계 ML 워크 플로를 구축, 배포 및 관리할 때
- Kubeflow는 여러 플랫폼에서 ML 학습, 초 매개 변수 조정, 워크로드를 자동으로 작업하려는 경우
[![image](https://user-images.githubusercontent.com/68671394/135788275-a8991bc9-f430-4010-a54b-34771223d755.png)](https://www.kubeflow.org/docs/started/kubeflow-overview/#interfaces)
### 디자인 예시
![image](https://user-images.githubusercontent.com/68671394/135787358-1e2e5995-7562-44d7-be6a-0dd3bcbd9c4d.png)

## NumPy_Pandas
