<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Covid data showcase</title>

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=figtree:400,600&display=swap" rel="stylesheet" />

    </head>
    <body class="antialiased">
        <div>
            <?php
               if(DB::connection()->getPdo()){
                echo "Connected to ".DB::connection()->getDatabaseName();
               };
            ?>
        </div>
        <div>
            {{"1. Cases in england today:"}}
            @foreach ($england as $item)
            {{$item->newCasesByDate}}
            @endforeach
        </div>

        <div>
            {{"2. Cases in England do not correlate with aggregate from NHS regions as those point towards hospital admissions, not new cases."}}
        </div>

        
        <div>
            {{"3. Age-group with the highest cases is: "}}
            {{$age_group}}
        </div>

        <div>
            {{"4. Region with fewest cases is: "}}
            {{$region_cases_least}}
            {{"--All region areas have 0 cases"}}
        </div>

        
        <div>
            {{"5. Area Code E12000005 points to: "}}
            @foreach ($area_code as $code)
            {{$code->AreaName}}
            @endforeach
        </div>
        
    </body>
</html>
