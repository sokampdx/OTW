<?
	$cookie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D');
	$default = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));
	$modify = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
	
	function xor_encrypt($in1, $in2) {
    	$text = $in1;
		$key = $in2;
    	$outText = '';

    	// Iterate through each character
    	for($i=0;$i<strlen($text);$i++) {
    		$outText .= $text[$i] ^ $key[$i % strlen($key)];
    	}		

    	return $outText;
	}

	print xor_encrypt($cookie, $default);
	print "\r\n";
	$realkey = "qw8J";

	print base64_encode(xor_encrypt($modify, $realkey));
	print "\r\n";
?>
