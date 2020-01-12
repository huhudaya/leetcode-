-- 627. 交换工资.sql
1.
	update salary set sex = char(ASCII(sex) ^ ASCII('m') ^ ASCII('f') );
2.	
	update salary set sex=if(sex = 'f', 'm','f');
3. 牛逼。。。
	update salary set sex = char(ascii('m') + ascii('f') - ascii(sex));
4.
	UPDATE salary
	SET
    	sex = CASE sex
        	WHEN 'm' THEN 'f'
        	ELSE 'm'
    	END;
