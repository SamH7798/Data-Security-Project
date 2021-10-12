<html>
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
  <h2>Admin Login</h2>
  <form action="/adminlogin" method="post">
    <div class="form-group">
      <label for="username">Name:</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Enter name"/>
    </div>
    <div class="form-group">
      <label for="password">Password:</label>
      <input type="password" class="form-control" id="password" name="password" placeholder="Enter password"/>    
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
<div>
<hr>


</div>
<hr/>

</body>
</html>
