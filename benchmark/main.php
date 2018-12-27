<?php
function main(array $args) : array
{
    $name = "world";
    if(array_key_exists('name', $args)) {
	$name = $args['name'];
    }
    return ["greeting" => "Hello $name!"];
}
