<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;
    /**
    * Show a list of all of the application's users.
    */
    public function index(): View
    {
        $england = DB::select('select * from covid_region_data');
 
        return view('show_data', ['england' => $england]);
    }
}
