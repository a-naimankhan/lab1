CREATE OR REPLACE PROCEDURE public.add_new_users(IN user_names text[], IN phone_numbers text[])
 LANGUAGE plpgsql
AS $procedure$
DECLARE
    i INTEGER := 1;
    incorrect_data TEXT[] := '{}';  
BEGIN
    WHILE i <= array_length(user_names, 1) LOOP
        IF phone_numbers[i] ~ '^\d{11}$' THEN             IF EXISTS (SELECT 1 FROM phonebook WHERE name = user_names[i]) THEN
                UPDATE phonebook SET phonenumber = phone_numbers[i] WHERE username = user_names[i];
            ELSE
                INSERT INTO phonebook(username, phonenumber) VALUES (user_names[i], phone_numbers[i]);
            END IF;
        ELSE
           incorrect_data := array_append(incorrect_data, user_names[i] || ' - ' || phone_numbers[i]);
        END IF;

        i := i + 1;
    END LOOP;


END; 

CREATE OR REPLACE PROCEDURE public.delete_users(IN thing character varying)
 LANGUAGE plpgsql
AS $procedure$
BEGIN
    IF thing IS NULL THEN
        RAISE NOTICE 'Nothing to delete';
        RETURN;
    ELSE
        DELETE FROM phonebook WHERE username = thing OR phonenumber = thing;
    END IF;
END;
$procedure$ 

CREATE OR REPLACE FUNCTION public.get_users_with_pagination(limit_count integer, offset_count integer)
 RETURNS TABLE(id integer, username character varying, phonenumber character varying)
 LANGUAGE plpgsql
AS $function$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.username, phonebook.phonenumber
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT limit_count OFFSET offset_count;
END;
$function$

CREATE OR REPLACE PROCEDURE public.insert_new_users(IN user_names text[], IN phone_numbers text[])
 LANGUAGE plpgsql
AS $procedure$
DECLARE
    i INTEGER := 1; 
    incorrect_data TEXT[] := '{}'; 
BEGIN
    
    WHILE i <= array_length(user_names, 1) LOOP
        
        IF phone_numbers[i] ~ '^\d{11}$' THEN
            
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = user_names[i]) THEN
                
                UPDATE phonebook SET phonenumber = phone_numbers[i] WHERE username = user_names[i];
            ELSE
                
                INSERT INTO phonebook (username, phonenumber) VALUES (user_names[i], phone_numbers[i]);
            END IF;
        ELSE
            
            incorrect_data := array_append(incorrect_data, user_names[i] || ' - ' || phone_numbers[i]);
        END IF;

        i := i + 1;  
    END LOOP;

    
    RAISE NOTICE 'Incorrect data: %', incorrect_data;

END;
$procedure$ 

CREATE OR REPLACE PROCEDURE public.insert_or_update_user(IN user_name text, IN user_phone text)
 LANGUAGE plpgsql
AS $procedure$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = user_name) THEN

        UPDATE phonebook SET phonenumber = user_phone WHERE username = user_name;
    ELSE

        INSERT INTO phonebook(username, phonenumber) VALUES (user_name, user_phone);
    END IF;
END;
$procedure$