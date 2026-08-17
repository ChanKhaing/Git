
<?php 
// echo 'oop concept and learning process ';

// echo 'hello world';

// $x = 10;
// var_dump($x);
// print ("hello world");
$age = 18;

// If-Else Statement
// if ($age >= 18) {
//     echo "မဲပေးခွင့်ရှိသည်။"; // Statement 1
// } else {
//     echo "မဲပေးခွင့်မရှိပါ။"; // Statement 2
// }

for ($i = 1; $i <= 5; $i++) {
    echo "အကြိမ်ရေ: $i <br>";
}

$count = 1;

while ($count <= 3) {
    echo "Count: $count <br>";
    $count++; // $count တန်ဖိုး မတိုးပေးရင် Infinite Loop (တန့်မသွားဘဲ ငြိ) ဖြစ်သွားပါမည်
}

$fruits = ["Apple", "Banana", "Orange"];
foreach ($fruits as $fruit) {
    echo "သစ်သီး: $fruit <br>";
}

function sayHello($name) {
    echo "မင်္ဂလာပါ $name";
}

sayHello("Aung Aung"); 
// Output: မင်္ဂလာပါ Aung Aung

function addNumbers($num1, $num2) {
    $result = $num1 + $num2;
    return $result; // တန်ဖိုးပြန်ထုတ်ပေးခြင်း
}

$sum = addNumbers(10, 20); // $sum ထဲသို့ 30 ရောက်ရှိမည်
echo $sum;

?>