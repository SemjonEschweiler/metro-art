import 'package:dio/dio.dart';
import 'package:metrocane/audioguide/audio_guide.dart';

class NetworkManager {
  final AudioGuide audioGuide = AudioGuide();

  NetworkManager();

  Future<String> processImageRequest(String base64Image) async {
    try {
      final dio = Dio();
      final response =
          await dio.post('https://metro-art-d6b2125924a4.herokuapp.com/process',
              data: base64Image,
              options: Options(
                contentType: 'text/plain',
              ));

      if (response.statusCode == 200) {
        String message = response.data["audio-description"];
        await audioGuide.speak(message);
        return message;
      } else {
        // Handle other status codes if needed

        String message =
            "Am Ende des Bahnsteigs in Fahrtrichtung Heiligenstadt befindet sich der Ausgang Schottenring mit einer auf und abwärtsführenden Fahrtreppe und einer mittig liegenden Stiege.";
        await audioGuide.speak(message);
        return "";
      }
    } catch (e) {
      String message =
          "Am Ende des Bahnsteigs in Fahrtrichtung Heiligenstadt befindet sich der Ausgang Schottenring mit einer auf und abwärtsführenden Fahrtreppe und einer mittig liegenden Stiege.";
      await audioGuide.speak(message);
      return "";
      // Handle Dio errors
    }
  }
}
