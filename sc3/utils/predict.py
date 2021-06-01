import pandas as pd

url = 'https://raw.githubusercontent.com/eeuunnjjiii/SC3-Project/master/sc3/franchise.csv'
data=pd.read_csv(url,sep=",")
data=data.sample(n=10)

#필요한 특성 추출
df=data.copy()
df=df[['업종','가맹점수','초기투자비용합계','평균매출액']]

#업종별 인코딩
df['업종']=df['업종'].replace('한식',1)
df['업종']=df['업종'].replace('서양식',2)
df['업종']=df['업종'].replace('분식',3)
df['업종']=df['업종'].replace('일식',4)
df['업종']=df['업종'].replace('중식',5)
df['업종']=df['업종'].replace('기타외국식',6)
df['업종']=df['업종'].replace('기타외식',7)

df['업종']=df['업종'].replace('치킨',8)
df['업종']=df['업종'].replace('피자',9)
df['업종']=df['업종'].replace('패스트푸드',10)
df['업종']=df['업종'].replace('커피',11)
df['업종']=df['업종'].replace('음료(커피 외)',12)
df['업종']=df['업종'].replace('아이스크림/빙수',13)
df['업종']=df['업종'].replace('제과제빵',14)
df['업종']=df['업종'].replace('주점',15)

#타겟 특성
target='평균매출액'

#이상치 제거
import numpy as np
df=df[df[target]<np.percentile(df[target], 99.5)]

#Hold-out 방식으로 훈련, 검증, 테스트 데이터셋 분리
from sklearn.model_selection import train_test_split
train,test=train_test_split(df,train_size=0.8, test_size=0.2, random_state=2)
train,val=train_test_split(train,train_size=0.8, test_size=0.2,random_state=2)

#데이터 특성/타겟 분리
features=train.drop(columns=[target]).columns
X_train=train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]
y_test = test[target]

#기준모델 생성
from sklearn.metrics import mean_absolute_error
y_pred=[y_train.mean()]*len(y_train)
mae=mean_absolute_error(y_train,y_pred)
#print('기준모델 MAE:',mae) > 165880

#머신러닝모델 생성
from xgboost import XGBRegressor
model = XGBRegressor(base_score=0.5, booster=None, colsample_bylevel=1,
             colsample_bynode=1, colsample_bytree=1, gamma=0, gpu_id=-1,
             importance_type='gain', interaction_constraints=None,
             learning_rate=0.2, max_delta_step=0, max_depth=7,
             min_child_weight=1, monotone_constraints=None,
             n_estimators=1000, n_jobs=-1, num_parallel_tree=1, random_state=2,
             reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
             tree_method=None, validate_parameters=False, verbosity=None)
model.fit(X_train, y_train)
#print('검증 데이터 스코어:',model.score(X_val, y_val)) > 0.564

#테스트 데이터 결과
y_test_pred=model.predict(X_test)
#print('테스트 데이터 MAE :', mean_absolute_error(y_test, y_test_pred)) > 104361
#print('테스트 데이터 R2 score :', r2_score(y_test, y_test_pred)) > 0.54339

#SHAP
import shap

def predict(업종,가맹점수,초기투자비용합계):

    # 함수 내에서 예측에 사용될 input을 만듭니다
    df = pd.DataFrame(
        data=[[업종,가맹점수,초기투자비용합계]], 
        columns=['업종','가맹점수','초기투자비용합계']
    )

    # 예측
    pred = model.predict(df)[0]

    # Shap value를 계산합니다
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(df)

    # Shap value, 특성이름, 특성값을 가지는 Series를 만듭니다
    feature_names = df.columns
    feature_values = df.values[0]
    shaps = pd.Series(shap_values[0], zip(feature_names, feature_values))


    result1 = format(int(explainer.expected_value), ',')
    result2 = format(int(pred), ',')
    result3 = shaps.to_string()


    # res = shaps.to_string()
    # res_print = res.split('\n')[0],'\n', res.split('\n')[1],'\n', res.split('\n')[2]
    return (result1, result2)


    # SHAP Force Plot
    # shap.initjs()
    # return shap.force_plot(
    #     base_value=explainer.expected_value, 
    #     shap_values=shap_values, 
    #     features=df
    # )

predict(1,263,47000)