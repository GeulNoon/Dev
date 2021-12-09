## **KoBART**를 이용한 문단 요약문 생성
학습하기 기능 중 요약하기 유형을 위해 KoBART를 이용하여 문단 속 핵심 문장을 추출하여 요약문을 생성해보았다.
##### **실행 방법**: colab에서 문장별로 실행
fine-tuning 전 모델로 요약할 경우 *!python train.py  --gradient_clip_val 1.0 --max_epochs 3 --default_root_dir logs  --gpus 1 --batch_size 4 --num_workers 2* 실행X
##### **필요 패키지**: 
파일(KoBART.ipynb) 코드 속
> !pip install git+https://github.com/SKT-AI/KoBART#egg=kobart
> !pip install -r requirements.txt
> !pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
> !pip install torchtext==0.8.0
을 실행하여 설치
###### **블로그 참조**: https://kimalgo.tistory.com/5?category=1052686
