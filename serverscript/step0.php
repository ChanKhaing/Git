<?php
// $age = readline("Enter your age: "); 

// echo "You are " . $age . " years old.";
// var_dump($age);
// print_r($age);

// $score = 20;
// if ($score >= 90) {
//     echo "Grade: A";
// } elseif ($score >= 80) {
//     echo "Grade: B";
// } elseif ($score >= 70) {
//     echo "Grade: C";
// } else {
//     echo "\nGrade: F";
// }
// $day=readline("\nEnter a day");


// // switch ($day) {
// //     case "Monday":
// //         echo "Start of the week!";
// //         break;
// //     case "Friday":
// //         echo "TGIF!";
// //         break;
// //     default:
// //         echo "Just another day.";
// // }


// switch ($score) 
// {
// case 20:
//     echo  "it is good/n";
//     break;
// default:
//     echo "not good/n";
// }

// $status = 200;

// // $message = match ($status) {
// //     200 => "OK",
// //     404 => "Not Found",
// //     500 => "Server Error",
// //     default => "Unknown Status",
// // };

// $message = match ($status) 
// {
//     200 => "ok",
//     default => "unknown status"
// };

// echo $message; 


// for loop (အကြိမ်ရေ အတိအကျ သိရင် သုံး)
// for ($i = 1; $i <= 5; $i++) {
//     echo "Number: $i \n"; // 1, 2, 3, 4, 5
// }

// while loop (အခြေအနေ မှန်နေသမျှ ဆက်လုပ်)
// $i = 1;
// while ($i <= 5) {
//     echo "While: $i \n";
//     $i++;
// }

// foreach (Array ထဲက အကြောင်းအရာတွေကို ဖတ်ဖို့)
// $colors = ["red", "green", "blue"];
// foreach ($colors as $color ) 
//     {
//         echo(" hello $color \n");
//     }


// // Key ပါယူချင်ရင်
// $user = [ 
//     "name" => "John",
//     "age" => 30,
//     "city" => "Yangon"
// ];
// foreach ($user as $key => $value)
//     {
//     echo "$key :$value \n";
//     }

// function sayHello($name ="Guest") {
//     echo "Hello, $name!";
// }

// // sayHello("Mg Mg");
// sayHello();

// function addNumbers(int $a, int $b): int {
//     return $a + $b;
// }

// echo addNumbers(5, 10);

// Arrow Function (PHP 7.4 က စပြီး ပါတယ် - တိုတောင်းတဲ့ function)
$multiply = fn( int $a, int $b) =>  $a * $b;
echo $multiply(3,5);

// Indexed Array (နံပါတ်စဉ်နဲ့ စာရင်း)
$fruits = ["Apple", "Banana", "Orange"];
echo $fruits[0]; // Apple
echo $fruits[1]; // Banana

// Associative Array (Key-Value အတွဲ)
$person = [
    "name" => "John",
    "age" => 30,
    "city" => "Yangon"
];
echo $person["name"]; // John

// Multidimensional Array (စာရင်းထဲမှာ စာရင်းထပ်)
$users = [
    ["name" => "John", "age" => 30],
    ["name" => "Su Su", "age" => 25],
];
echo $users[1]["name"]; // Su Su

// Array Functions (အသုံးများတဲ့ array လုပ်ဆောင်ချက်များ)
$numbers = [1, 2, 3, 4, 5];

// Count - စာရင်းထဲက အရေအတွက်
echo count($numbers); // 5

// Push - နောက်ဆုံးမှာ ထပ်ထည့်
array_push($numbers, 6); // [1,2,3,4,5,6]

// Pop - နောက်ဆုံးက ဖယ်ထုတ်
array_pop($numbers); // [1,2,3,4,5]

// Merge - စာရင်းနှစ်ခု ပေါင်းစပ်
$more = [6, 7, 8];
$all = array_merge($numbers, $more); // [1,2,3,4,5,6,7,8]

// In Array - ရှိမရှိ စစ်
if (in_array(3, $numbers)) {
    echo "3 is in the list!";
}
?>


