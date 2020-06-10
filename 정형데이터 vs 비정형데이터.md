# 정형데이터 vs 비정형데이터   
Assembled by Sohyeon Yim (2020-06-11)   

'수집 데이터 형태'에 따라 정형 데이터, 반정형 데이터, 비정형 데이터로 나눌 수 있다.   

## 정형 데이터(Structured Data)   
-컬럼이 스키마에 의해 정의되어 있다.      
-행과 열이 구분되어 있다. -> SQL 기반 연산 가능   
-e.g. RDBMS의 테이블들(단일 테이블 혹은 조인한 테이블 포함), 스프레드시트   
<pre>
<code>
SELECT NAME FROM STUDENT WHERE AGE BETWEEN 20 AND 25
</code>
</pre>
![정형데이터 구조](https://user-images.githubusercontent.com/44013936/84292280-24844300-ab81-11ea-9c1a-7930b6d48015.gif)   

## 반정형 데이터(Semi-Structured Data)   
-데이터 내부에 정형데이터의 스키마에 해당되는 메타데이터를 갖고 있다. (cf. 정형데이터는 데이터의 스키마 정보를 관리하는 DBMS와 데이터 내용이 저장되는 데이터 저장소로 구분)   
-일반적으로 파일 형태로 저장된다.   
-데이터 내부에 있는 규칙성을 파악해 데이터를 파싱할 수 있는 파싱 규칙을 적용한다.   
-e.g. URL 형태로 존재(HTML), 오픈 API 형태로 제공(XML, JSON), 로그 형태(웹로그, IOT에서 제공하는 센서 데이터)   
![반정형 데이터](https://user-images.githubusercontent.com/44013936/84293560-eb4cd280-ab82-11ea-9251-944d2745ccf4.gif)   

## 비정형 데이터(Unstrudtured Data)   
-데이터 세트가 아닌 하나의 데이터가 수집 데이터로 객체화돼 있다.   
-데이터를 파싱해 탐색한다.   
-e.g. 텍스트, 이미지, 동영상 등   


## Reference & Additional Resources
http://www.dbguide.net/db.db?cmd=view&boardUid=186813&boardConfigUid=9&categoryUid=216&boardIdx=152&boardStep=1
