<?php

// class Car {
//     // Properties
//     public $brand;
//     public $color;

//     // Method
//     public $this->brand = $brand;
//     public function drive() {
//         return "The " . $this->brand . " is driving!";
//     }
// }

// // Object ဖန်တီးပြီး သုံးစွဲခြင်း
// $car1 = new Car();
// $car1->brand = "Toyota"; // Property သို့ တန်ဖိုးထည့်ခြင်း

// echo $car1->drive();    // Output: The Toyota is driving!




class Fruit {
  // Properties
  public $name;
  public $color;

  // Method to set the properties
  function set_details($name, $color) {
    $this->name = $name;
    $this->color = $color;
  }

  // Method to display the properties
  function get_details() {
    echo "Name: " . $this->name . ". Color: " . $this->color .".<br>";
  }
}

$fruit1 = new Fruit();
$fruit1->set_details("Apple", "Red");
$fruit1->get_details(); // Output: Name: Apple. Color: Red.


?>