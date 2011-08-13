<?php

$base_dir = "/home/groups/k/kx/kxstudio/htdocs/paste/";

function downloadFile($fullPath) {
  // Must be fresh start
  if(headers_sent())
    die('Headers Sent');

  // Required for some browsers
  if(ini_get('zlib.output_compression')) 
    ini_set('zlib.output_compression', 'Off'); 

  $fsize = filesize($fullPath);

  header("Pragma: public"); // required
  header("Expires: 0");
  header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
  header("Cache-Control: private",false); // required for certain browsers
  header("Content-Type: application/force-download");
  header("Content-Disposition: attachment; filename=\"".basename($fullPath)."\";" );
  header("Content-Transfer-Encoding: binary");
  header("Content-Length: ".$fsize);
  ob_clean();
  flush();
  readfile($fullPath);
}

if (!empty($_GET["id"])) {
  $paste_id   = htmlspecialchars($_GET["id"]);
  $paste_file = $base_dir . "repo/" . $paste_id;

  if (!file_exists($paste_file)) die("File does not exist");

  downloadFile($paste_file);
}

?>
