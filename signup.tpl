<html>
<Style>
Details{
  padding:5px;
}

h2{
  text-align:center;
  background-color: rgba(135,206,235,.3);
    background-blend-mode: multiply;
    background-size: cover;
    padding-bottom: 30px;
}
</Style>
<header>
  <title>COVID Web Collector</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</header>

<body>
<div class="container">
  <h2>Sign Up</h2>
  <form action="/signup" method="post">
    <div class="form-group">
      <label for="username">UserName:</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Enter Userpage"/>
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Enter Password"/>    
    </div>
    <div class="form-group">
      <label for="name">Name:</label>
      <input type="text" class="form-control" id="name" name="name" placeholder="Enter Name"/>    
    </div>
    <div class="form-group">
      <label for="email">Email:</label>
      <input type="text" class="form-control" id="email" name="email" placeholder="Enter Email"/>    
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>



</div>
<hr/>

</body>
</html>
