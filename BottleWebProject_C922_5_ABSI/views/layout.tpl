<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <nav class="navbar navbar-custom navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/">
          <!-- ����������� ���� ����� -->
          <img src="static\images\home\logo.png" alt="logo" style="width:75px;height:24px;">
          </a>
        </div>
        <!-- ����������� ������-������ ��������� ���� -->
        <ul class="nav navbar-nav">
            <li><a class="navbar-brand" href="/home">Homepage</a></li><!-- ������-������ ����� -->
            <li><a class="navbar-brand" href="/about">About</a></li><!-- ������-������ ����� -->
        </ul>
      </div>
    </nav>

    <!-- ����������� ����� �������� -->
    <div class="container body-content">
        {{!base}}
        <footer>
            <p14>&copy; {{ year }} - KVAS Corporation</p14>
        </footer>
    </div>
    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
