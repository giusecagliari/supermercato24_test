<?php
/**
 * Created by PhpStorm.
 * User: Giuseppe
 * Date: 26/10/2018
 * Time: 19:12
 */

class Path
{
    public $currentPath;

    function __construct($path)
    {
        $this->currentPath = $path;
    }


    public function cd(string $newPath)
    {
        $hiearchy = explode('/', $this->currentPath);
        unset($hiearchy[0]);
        $this->checkNameDirectory($hiearchy);

        $addedHiearchy = explode('/', $newPath);
        foreach ($addedHiearchy as $value) {
            if ($value === '..') {
                array_pop($hiearchy);
            } else {
                array_push($hiearchy, $value);
            }
        }

        $this->currentPath = $this->generatePath($hiearchy);
    }

    public function generatePath(array $hiearchy)
    {
        $path = '';
        foreach ($hiearchy as $value) {
            $path .= '/' . $value;
        }

        return $path;
    }

    public function checkNameDirectory(array $hiearchy)
    {
        foreach ($hiearchy as $value) {
            if (preg_match('[A-Z]', $value) || preg_match('[a-z]', $value)) {
                throw new Exception('directory should be a-z or A-Z');
            }
        }

    }
}

$path = new Path('/a/b/c/d');
$path->cd('../x');
echo $path->currentPath;