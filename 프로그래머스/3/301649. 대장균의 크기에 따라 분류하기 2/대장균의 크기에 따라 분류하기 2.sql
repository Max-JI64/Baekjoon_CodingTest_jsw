-- 개체의 크기를 상위 몇%로 산정할려면
-- 총 대장균의 데이터 개수, 순위가 필요하다
-- 이것을 백분율로 만든다

WITH TEMP AS (
    SELECT ID, 
            (ROW_NUMBER() OVER(ORDER BY SIZE_OF_COLONY DESC)) / (COUNT(*) OVER()) AS RATIO
    FROM ECOLI_DATA
)
-- 그 결과 각각의 데이터엔 RATIO가 생겼다
SELECT ID, 
        CASE
            WHEN RATIO<=0.25 THEN "CRITICAL"
            WHEN RATIO<=0.5 THEN "HIGH"
            WHEN RATIO<=0.75 THEN "MEDIUM"
            ELSE "LOW"
        END AS COLONY_NAME
FROM TEMP
ORDER BY ID;