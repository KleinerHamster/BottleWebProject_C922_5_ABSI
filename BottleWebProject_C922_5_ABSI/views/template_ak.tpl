%rebase('layout.tpl', title='mcm_system_reliability', year=2022)
<!--��������� �������� - ��������-->
<div>
    <p><br></p>
    <!-- ��������� ����� - ������� ��������-->
    <headerParagraphAbout class="A">Evaluation of the reliability of the simplest systems by the Monte Carlo method<br></headerParagraphAbout>
    <!--��������� �� ������-->
    <hr >
    </hr>
</div>

<table class="tbV"><!--�������-->
    <caption><headerHP2>Probabilities of elements:</headerHP2></caption>
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

<headerHP2>Number of tests: {{N_str}}</headerHP2>

<hr></hr>

<table class="tbV"><!--�������-->
    <caption><headerHP2>Probability of uptime:</headerHP2></caption>
    <tr><!--����� �������-->
        <th>P*</th>
        <th>P1</th>
        <th>P2</th>
        <th>P</th>
        <th>P-P*</th>
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

<headerHP2>Test results:</headerHP2>

<!--������� � ������� �����-->
{{!html}}

<!--��������� �� ������-->
<p><br></p>
<hr class="about"></hr>
