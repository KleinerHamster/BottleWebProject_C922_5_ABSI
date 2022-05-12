<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Simulation Modeling</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>

</head>

<body>
    <nav class="navbar navbar-custom navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">
          <!-- отображение лого сайта -->
           <img src="static\images\home\logo.png" alt="logo" style="width:80px;height:28px;">
          </a>
        </div>
        <!-- отображение кнопок-ссылок основного меню -->
        <ul class="nav navbar-nav">
            <li><a class="navbar-brand" href="/home">Simulation modeling</a></li><!-- кнопка-ссылка на главную страницу -->


            <li><a class="navbar-brand" href="/contact">Anya</a></li><!-- кнопка-ссылка домой -->
            <li><a class="navbar-brand" href="/vi">Vi</a></li><!-- кнопка-ссылка домой -->
            <li><a class="navbar-brand" href="/sonya">Sonya</a></li><!-- кнопка-ссылка домой -->
            <li><a class="navbar-brand" href="/kama">Kama</a></li><!-- кнопка-ссылка домой -->

            <li><a class="navbar-brand" href="/about">About us</a></li><!-- кнопка-ссылка на страцу об авторах -->
            
        </ul>
      </div>
    </nav>

    <!-- отображение внизу компании -->
    <div class="container body-content">
        {{!base}}
        <footer>
            <pEnd>&copy; {{ year }} - KVAS Corporation</pEnd>
        </footer>
    </div>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
