<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
class covidDataController extends Controller
{
    //
    public function england()
    {
        //get record of englanbd from database
        $england = DB::table('covid_region_data')
                    ->where('areaName', '=', "England")
                    ->get();

        $age_group = DB::table('patients')
                ->select('age',DB::raw('COUNT(age) AS occurrences'))
                ->groupBy('age')
                ->orderBy('occurrences', 'DESC')
                ->limit(1)
                ->get();

        $region_cases_least = DB::table('covid_region_data')
            ->where([
                ['areaType','=','region'],
                ['newCasesByDate','>=',1]])
            ->orderBy('newCasesByDate', 'asc')
            ->limit(1)
            ->get();

        //area code
        $area_code = DB::table('covid_region_data')
            ->where('areaCode', '=', "E12000005")
            ->get();
            
        // $counted = array_count_values($age);
        // $number_appears_most = array_keys($counted);
        // $highest_age = $number_appears_most[0];
        //$england = DB::select("select * from covid_region_data where newCasesByDate England");
        // $england = DB::select("select newCasesByDate from covid_region_data")->where("areaName","England");

        return view('show_data',compact('england','age_group','region_cases_least','area_code'));
    }
}
