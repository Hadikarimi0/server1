<?php

ob_start();
$load = sys_getloadavg();
error_reporting(0);
ini_set( "log_errors","Off" );
define('API_KEY',"7500213824:AAFTKrUfHp8ixxcz1XgfrpizCmFlJ0zHMbY");
function METI($method,$datas=[]){
 $url = "https://api.telegram.org/bot".API_KEY."/".$method;
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
$res = curl_exec($ch);
if(curl_error($ch)){
var_dump(curl_error($ch));
}else{
return json_decode($res);
}
}
function SendMessage($chat_id, $text){
METI('sendMessage',[
'chat_id'=>$chat_id,
'text'=>$text,
'parse_mode'=>'MarkDown']);
}

$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$chat_id = $update->message->chat->id;
$from_id = $update->message->from->id;
$text = $update->message->text;


if($text=="/start"){
 METI('sendmessage',[
                'chat_id'=>$chat_id,
                'text'=>"ربات انتقال یافت.",
]);
}else{
SendMessage($from_id,"ربات انتقال یافت.","HTML");}
unlink('error_log');
?>
