import 'package:flutter_tts/flutter_tts.dart';

class AudioGuide {
   FlutterTts flutterTts = FlutterTts();

  Future<void> speak(String text) async {
    await flutterTts.setSharedInstance(true);

    await flutterTts.setLanguage("DE");
    await flutterTts.speak(text);
  }
}
