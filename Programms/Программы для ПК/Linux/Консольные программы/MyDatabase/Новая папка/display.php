<?php
use LDAP\Result;

include 'dbconnection.php';

?>
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>crud operation</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

</head>
<body>
<div class = "container" >

<button class="btn btn-primary my-5" >

<a href="user.php" class="text-light">add user</a>

</button>

<table class="table">
  <thead>
    <tr>
      <th scope="col">id</th>
      <th scope="col">name</th>
      <th scope="col">email</th>
      <th scope="col">mobile</th>
      <th scope="col">password</th>
      <th scope="col">operations</th>
      
    </tr>
  </thead>
  <tbody>

<?php
$sql = "select * from `crud` ";
$result = mysqli_query($con,$sql);
if($result)
{
while($row = mysqli_fetch_assoc($result))
{

$id = $row['id'];

$name = $row['name'];

$email = $row['email'];

$mobile = $row['mobile'];

$password = $row['password'];

echo'<tr>
<th scope = " row">'.$id.'<th>
<th scope = " row">'.$name.'<th>
<th scope = " row">'.$email.'<th>
<th scope = " row">'.$mobile.'<th>
<th scope = " row">'.$password.'<th>

<button class="btn btn-primary my-5" >

<a href="user.php" class="text-light">update</a>

</button>
<button class="btn btn-primary my-5" >

<a href="user.php" class="text-light">delete</a>
</button>
</tr>';

}
}




?>

  </tbody>
</table>

<div>

</body>
</html>