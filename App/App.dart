import 'package:flutter/material.dart';
import 'dart:math'; // pow()

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Calculadora de Perímetro e Área",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: "Calculadora de Perímetro e Área"),
    );
  }
}

class MyHomePage extends StatefulWidget {
  // Construtor "antigo"
  // MyHomePage({Key? key, this.title}) : super(key: key);

  MyHomePage({super.key, this.title = ''});

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  // Atributos
  
  double _area = 0.0; 
  double _perimetro = 0.0;
  double _a = 0.0;
  double _b = 0.0;
  double _c = 0.0;

  final aController = TextEditingController();
  final bController = TextEditingController();
  final cController = TextEditingController();

  // Construtor
  _MyHomePageState();

  // Métodos
  void _calcularImc() { 
    _a = double.parse(aController.text);
    _b = double.parse(bController.text);
    _c = double.parse(cController.text);
    if (_a<_b+_c && _b<_a+_c && _c<_a+_b) {
    _perimetro = _a+_b+_c;
    double _s = _perimetro/2;
    _area = sqrt(_s*(_s-_a)*(_s-_b)*(_s-_c));  
      aController.text = "";
      bController.text = "";
      cController.text = "";
      setState(() {});
    }
  } // _calcular()

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(
        padding: EdgeInsets.all(16.0),
        child: Column(
          // mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
              child: Text(
                "Dados:",
                style: textFieldTextStyle(),
              ),
            ),
            // --- Lado A ---
            Padding(
              padding: EdgeInsets.all(5),
              child: textField("Lado A", aController),
              ),
            
            // --- Lado B ---
            Padding(
              padding: EdgeInsets.all(5),
              child: textField("Lado B", bController),
            ),
            // --- Lado C ---
            Padding(
              padding: EdgeInsets.all(5),
              child: textField("Lado C", cController),
            ),
            // Saída
            Padding(
              padding: EdgeInsets.fromLTRB(5, 5, 5, 20),
              child: Text("${_perimetro.toStringAsFixed(1)}"),
            ),
            // Saída
            Padding(
              padding: EdgeInsets.fromLTRB(5, 5, 5, 20),
              child: Text("${_area.toStringAsFixed(1)}"),
            ),
            ElevatedButton(
              child: Text(
                "Calcular IMC",
                style: textFieldTextStyle(),
              ),
              onPressed: _calcularImc,
            ),
            
          ],
        ),
      ),
    );
  }

  TextStyle textFieldTextStyle() {
    return TextStyle(fontSize: 20.0);
  }

  Widget textField(String texto, TextEditingController controller) {
    return TextField(
      keyboardType: TextInputType.number,
      decoration: InputDecoration(
        border: OutlineInputBorder(),
        labelText: texto,
        hintText: texto,
      ),
      style: textFieldTextStyle(),
      controller: controller,
    );
  }
}
