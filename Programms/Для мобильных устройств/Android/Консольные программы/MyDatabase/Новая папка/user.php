<?php
include 'dbconnection.php';
if(isset($_POST['submit']))
{
$name =$_POST['name'];
$email = $_POST['email'];
$mobile = $_POST['mobile'];
$password = $_POST['password'];

$sql = "insert into `crud` (name,email,mobile,password)
values('$name','$email','$mobile','$password')";
$result = mysqli_query($con, $sql);
if($result)
{
echo"данные добавлены!";



}
else{
    die(mysqli_error($con));
}

}


?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

    <title>CRUD</title>
  </head>
  <body>
      <div class = "container">
      <form method="POST">
          
  <div class="form-group">
    <label >Имя пользователя</label>
    <input type="text" class="form-control"
    placeholder="введи имя"
    name = "name" autocomplete = "off";>
  </div>

  <div class="form-group">
    <label >Почта</label>
    <input type="email" class="form-control"
    placeholder = "введи почту"
    name = "email" autocomplete = "off";>
    </div>

  <div class="form-group">
    <label >телефон</label>
    <input type="text" class="form-control"
    placeholder="телефон" name = "mobile" autocomplete="off">
</div>

  </div>
  <div class="form-group">
    <label>Пароль</label>
    <input type="text" class="form-control"
    placeholder = "введи пароль"
    name="password">
  </div>

  <button type="submit" class="btn btn-primary" name = "submit">Submit</button>
  
</form>

</div>

  </body>
</html>