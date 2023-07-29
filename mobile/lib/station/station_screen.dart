import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_beacon/flutter_beacon.dart';
import 'package:flutter_reactive_ble/flutter_reactive_ble.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:get/get.dart';
import 'package:vibration/vibration.dart';

import '../bluetooth/requirenment_controller.dart';

enum Direction { left, right, top, bottom, none }

class SubwayStationScreen extends StatefulWidget {
  FlutterTts flutterTts = FlutterTts();
  Direction direction = Direction.none;
  final flutterReactiveBle = FlutterReactiveBle();

  SubwayStationScreen({super.key});

  @override
  // ignore: library_private_types_in_public_api
  _SubwayStationScreenState createState() => _SubwayStationScreenState();
}

class _SubwayStationScreenState extends State<SubwayStationScreen> {
  double xWhiteCirclePosition = 0;
  double yWhiteCirclePosition = 0;
  final controller = Get.find<RequirementStateController>();
  StreamSubscription<RangingResult>? _streamRanging;
  final _regionBeacons = <Region, List<Beacon>>{};
  final _beacons = <Beacon>[];

  @override
  void initState() {
    super.initState();

    initScanBeacon();
  }

  @override
  Widget build(BuildContext context) {
    // Access the Theme here inside the build method
    ThemeData theme = Theme.of(context);

    // Calculate initial position of the white circle in the middle of the black circle
    double initialXWhiteCirclePosition =
        MediaQuery.of(context).size.width / 2 - 75;
    double initialYWhiteCirclePosition =
        MediaQuery.of(context).size.height / 2 - 75;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Stephanplatz'),
      ),
      body: Stack(
        children: [
          // Fullscreen Black Circle
          IgnorePointer(
            // Make the black circle non-swipeable
            child: Container(
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: theme.primaryColor, // Use the theme here
              ),
            ),
          ),
          // Moving White Circle
          Positioned(
            left: initialXWhiteCirclePosition + xWhiteCirclePosition,
            top: initialYWhiteCirclePosition + yWhiteCirclePosition,
            child: GestureDetector(
              onPanUpdate: (details) {
                print('dx ${details.delta.dx}');
                print('dy ${details.delta.dy}');

                setDirection(details.delta.dx, details.delta.dy);

                setState(() {
                  xWhiteCirclePosition += details.delta.dx;
                  yWhiteCirclePosition += details.delta.dy;
                });
              },
              onPanEnd: (details) {
                onDirectionChanged(widget.direction);
                setState(() {
                  xWhiteCirclePosition = 0;
                  yWhiteCirclePosition = 0;
                });
                // Calculate the direction and call the callback
              },
              child: Container(
                width: 150,
                height: 150,
                decoration: const BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.white,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  void setDirection(double dx, double dy) {
    if (dx > 1.0) {
      widget.direction = Direction.right;
      return;
    }
    if (dx < -1.0) {
      widget.direction = Direction.left;
      return;
    }
    if (dy < -1.0) {
      widget.direction = Direction.top;
      return;
    }
    if (dy > 1.0) {
      widget.direction = Direction.bottom;
      return;
    }
  }

  void findController() {
    widget.flutterReactiveBle.scanForDevices(withServices: [Uuid.parse("")], scanMode: ScanMode.lowLatency).listen((device) {
      //code for handling results
    }, onError: () {
      //code for handling error
    });
  }

  void onDirectionChanged(Direction direction) async {
    // -y ==== top
    // +y ==== bottom
    // +x ==== right
    // -x ==== left

    await widget.flutterTts.setSharedInstance(true);

    await widget.flutterTts.setLanguage("DE");
    await widget.flutterTts.speak(
        "Die U-Bahn-Station Oberlaa ist die südliche Endstation der Wiener U-Bahn-Linie U1");

    // Handle the direction change here, you can print it or do anything you want
    print("Direction changed: $direction");
  }

  initScanBeacon() async {
    print("LS ${await flutterBeacon.requestAuthorization}");

    try {
      // if you want to manage manual checking about the required permissions
      await flutterBeacon.initializeScanning;

      // or if you want to include automatic checking permission
      await flutterBeacon.initializeAndCheckScanning;
    } on PlatformException catch (e) {
      print("Exception happened: $e");
    }

    final regions = <Region>[
      Region(
        identifier: 'Alt',
      ),
    ];

    if (_streamRanging != null) {
      if (_streamRanging!.isPaused) {
        _streamRanging?.resume();
        return;
      }
    }

    _streamRanging =
        flutterBeacon.ranging(regions).listen((RangingResult result) {
      print(result);
      if (mounted) {
        setState(() {
          _regionBeacons[result.region] = result.beacons;
          _beacons.clear();
          _regionBeacons.values.forEach((list) {
            if (list.isNotEmpty) {
              final beacon = list[0].accuracy < 2.5;
              if(beacon) {
                Vibration.vibrate();
              }
            }
          });
        });
      }
    });
  }
}
