-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
IF(FREEZER_YN IS NULL, 'N', FREEZER_YN)
FROM FOOD_WAREHOUSE
WHERE SUBSTR(TLNO, 1, 3) = '031' 
ORDER BY WAREHOUSE_ID