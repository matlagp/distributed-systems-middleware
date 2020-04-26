#ifndef HOME_ICE
#define HOME_ICE

module Home {
    exception InvalidOperationException{};
    exception AlreadyOnException extends InvalidOperationException{};
    exception AlreadyOffException extends InvalidOperationException{};

    exception NoDataException{};

    interface Device {
        void on() throws AlreadyOnException;
        void off() throws AlreadyOffException;
    }

    struct CCTVStatus {
        int theta;
        int zoom;
    }

    interface CCTV extends Device {
        void zoomIn(int zoom);
        void zoomOut(int zoom);
        void tiltLeft(int theta);
        void tiltRight(int theta);

        CCTVStatus getStatus();
    }

    sequence<double> Readings;

    interface Sensor extends Device {
        double getLastReading() throws NoDataException;
        Readings getReadings() throws NoDataException;
    }

    interface LightSensor extends Sensor{};
    interface SoundSensor extends Sensor{};
}

#endif