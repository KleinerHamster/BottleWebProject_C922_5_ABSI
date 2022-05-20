<br><img src="static\images\home\logo.png" alt="logo" style="width:80px;height:28px;">
<!--��������� �������� - ��������-->
<div>
    <!-- ��������� ����� - ������� ��������-->
    <headerParagraphAbout class="A">Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerParagraphAbout>
    <!--��������� �� ������-->
    <hr >
    </hr>
</div>
<!--���������� ����������� ������-->
<headerMCM32>Number of tests: {{N_str}}</headerMCM32>
<table class="tbV"><!--������� -->

    <caption><headerA1>Probabilities of elements:</headerA1></caption>
    <tr><!--����� �������-->
        <th>A</th>
        <th>B</th>
        <th>C</th>
        <th>D</th>
        <th>E</th>
    </tr>
    <tr><!--������ ��� ����� -->
        <td>{{A_str}}</td>
        <td>{{B_str}}</td>
        <td>{{C_str}}</td>
        <td>{{D_str}}</td>
        <td>{{E_str}}</td>
    </tr>
</table>

<hr></hr>

<table class="tbV"><!--�������-->
    <caption><headerA1>Probability of uptime:</headerA1></caption>
    <tr><!--����� �������-->
        <th>P*</th>
        <th>P1</th>
        <th>P2</th>
        <th>P</th>
        <th>|P-P*|</th>
    </tr>
    <tr><!--������ ��� ����� -->
        <td>{{round(p_star,3)}}</td>
        <td>{{round(p1, 3)}}</td>
        <td>{{round(p2, 3)}}</td>
        <td>{{round(p, 3)}}</td>
        <td>{{round(p_pStar,3)}}</td>
    </tr>
</table>

<!--��������� �� ������-->
<hr></hr>

<headerMCM32>Test results:</headerMCM32>

<!--������� � ������� �����-->
{{!html}}

%import datetime
%today = datetime.datetime.today()
%printToday = today.strftime("%H:%M:%S %d.%m.%Y")

<!--��������� �� ������-->
<hr class="about"></hr>
<div class="container body-content">
    <footer>
        <pEnd>&copy; {{printToday}} - KVAS Corporation</pEnd>
    </footer>
</div>
