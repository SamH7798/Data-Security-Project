<html>
<header>
  <title>COVID Web Collector</title>
  <meta charset="utf-8">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</header>

<style>
table, th, td {
    border: 1px solid black;
    padding:0.5rem;
    text-align:center;
    margin-left:auto;
    margin-right:auto;
}

h2{
    text-align:center;
  background-color: rgba(135,206,235,.3);
    background-blend-mode: multiply;
    background-size: cover;
    padding-bottom: 30px;
}
</style>
</head>

<body>
<div class="container">
  <h2>Covid Info</h2>
<hr>
<table>
% i = 0
<tr><td>name</td> <td>age</td> <td>symthom1</td> <td>symthom2</td> </tr>
%while i < len(names):
    
    <tr><td>{{names[i]}}</td> <td>{{ages[i]}}</td> <td>{{symthom1s[i]}}</td> <td>{{symthom2s[i]}}</td> </tr>
%    i = i + 1
% end

</table>
<hr>
<form method="get" action= "/login"><button type= "submit" class="btn btn-primary">Log Out</button></form>

</div>


</body>
</html>
