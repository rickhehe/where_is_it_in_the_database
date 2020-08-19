select table_name
       ,column_name

  from information_schema.columns
 
 where true
       and table_schema ~* 'public'
       and table_name ~* ''
       and column_name ~* ''
 
 order by table_name
