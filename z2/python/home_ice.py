# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.3
#
# <auto-generated>
#
# Generated from file `home.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Home
_M_Home = Ice.openModule('Home')
__name__ = 'Home'

if 'InvalidOperationException' not in _M_Home.__dict__:
    _M_Home.InvalidOperationException = Ice.createTempClass()
    class InvalidOperationException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::InvalidOperationException'

    _M_Home._t_InvalidOperationException = IcePy.defineException('::Home::InvalidOperationException', InvalidOperationException, (), False, None, ())
    InvalidOperationException._ice_type = _M_Home._t_InvalidOperationException

    _M_Home.InvalidOperationException = InvalidOperationException
    del InvalidOperationException

if 'AlreadyOnException' not in _M_Home.__dict__:
    _M_Home.AlreadyOnException = Ice.createTempClass()
    class AlreadyOnException(_M_Home.InvalidOperationException):
        def __init__(self):
            _M_Home.InvalidOperationException.__init__(self)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::AlreadyOnException'

    _M_Home._t_AlreadyOnException = IcePy.defineException('::Home::AlreadyOnException', AlreadyOnException, (), False, _M_Home._t_InvalidOperationException, ())
    AlreadyOnException._ice_type = _M_Home._t_AlreadyOnException

    _M_Home.AlreadyOnException = AlreadyOnException
    del AlreadyOnException

if 'AlreadyOffException' not in _M_Home.__dict__:
    _M_Home.AlreadyOffException = Ice.createTempClass()
    class AlreadyOffException(_M_Home.InvalidOperationException):
        def __init__(self):
            _M_Home.InvalidOperationException.__init__(self)

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::AlreadyOffException'

    _M_Home._t_AlreadyOffException = IcePy.defineException('::Home::AlreadyOffException', AlreadyOffException, (), False, _M_Home._t_InvalidOperationException, ())
    AlreadyOffException._ice_type = _M_Home._t_AlreadyOffException

    _M_Home.AlreadyOffException = AlreadyOffException
    del AlreadyOffException

if 'NoDataException' not in _M_Home.__dict__:
    _M_Home.NoDataException = Ice.createTempClass()
    class NoDataException(Ice.UserException):
        def __init__(self):
            pass

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Home::NoDataException'

    _M_Home._t_NoDataException = IcePy.defineException('::Home::NoDataException', NoDataException, (), False, None, ())
    NoDataException._ice_type = _M_Home._t_NoDataException

    _M_Home.NoDataException = NoDataException
    del NoDataException

_M_Home._t_Device = IcePy.defineValue('::Home::Device', Ice.Value, -1, (), False, True, None, ())

if 'DevicePrx' not in _M_Home.__dict__:
    _M_Home.DevicePrx = Ice.createTempClass()
    class DevicePrx(Ice.ObjectPrx):

        def on(self, context=None):
            return _M_Home.Device._op_on.invoke(self, ((), context))

        def onAsync(self, context=None):
            return _M_Home.Device._op_on.invokeAsync(self, ((), context))

        def begin_on(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.Device._op_on.begin(self, ((), _response, _ex, _sent, context))

        def end_on(self, _r):
            return _M_Home.Device._op_on.end(self, _r)

        def off(self, context=None):
            return _M_Home.Device._op_off.invoke(self, ((), context))

        def offAsync(self, context=None):
            return _M_Home.Device._op_off.invokeAsync(self, ((), context))

        def begin_off(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.Device._op_off.begin(self, ((), _response, _ex, _sent, context))

        def end_off(self, _r):
            return _M_Home.Device._op_off.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.DevicePrx.ice_checkedCast(proxy, '::Home::Device', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.DevicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::Device'
    _M_Home._t_DevicePrx = IcePy.defineProxy('::Home::Device', DevicePrx)

    _M_Home.DevicePrx = DevicePrx
    del DevicePrx

    _M_Home.Device = Ice.createTempClass()
    class Device(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Home::Device', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::Device'

        @staticmethod
        def ice_staticId():
            return '::Home::Device'

        def on(self, current=None):
            raise NotImplementedError("servant method 'on' not implemented")

        def off(self, current=None):
            raise NotImplementedError("servant method 'off' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_DeviceDisp)

        __repr__ = __str__

    _M_Home._t_DeviceDisp = IcePy.defineClass('::Home::Device', Device, (), None, ())
    Device._ice_type = _M_Home._t_DeviceDisp

    Device._op_on = IcePy.Operation('on', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, (_M_Home._t_AlreadyOnException,))
    Device._op_off = IcePy.Operation('off', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, (_M_Home._t_AlreadyOffException,))

    _M_Home.Device = Device
    del Device

if 'CCTVStatus' not in _M_Home.__dict__:
    _M_Home.CCTVStatus = Ice.createTempClass()
    class CCTVStatus(object):
        def __init__(self, theta=0, zoom=0):
            self.theta = theta
            self.zoom = zoom

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.theta)
            _h = 5 * _h + Ice.getHash(self.zoom)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Home.CCTVStatus):
                return NotImplemented
            else:
                if self.theta is None or other.theta is None:
                    if self.theta != other.theta:
                        return (-1 if self.theta is None else 1)
                else:
                    if self.theta < other.theta:
                        return -1
                    elif self.theta > other.theta:
                        return 1
                if self.zoom is None or other.zoom is None:
                    if self.zoom != other.zoom:
                        return (-1 if self.zoom is None else 1)
                else:
                    if self.zoom < other.zoom:
                        return -1
                    elif self.zoom > other.zoom:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_CCTVStatus)

        __repr__ = __str__

    _M_Home._t_CCTVStatus = IcePy.defineStruct('::Home::CCTVStatus', CCTVStatus, (), (
        ('theta', (), IcePy._t_int),
        ('zoom', (), IcePy._t_int)
    ))

    _M_Home.CCTVStatus = CCTVStatus
    del CCTVStatus

_M_Home._t_CCTV = IcePy.defineValue('::Home::CCTV', Ice.Value, -1, (), False, True, None, ())

if 'CCTVPrx' not in _M_Home.__dict__:
    _M_Home.CCTVPrx = Ice.createTempClass()
    class CCTVPrx(_M_Home.DevicePrx):

        def zoomIn(self, zoom, context=None):
            return _M_Home.CCTV._op_zoomIn.invoke(self, ((zoom, ), context))

        def zoomInAsync(self, zoom, context=None):
            return _M_Home.CCTV._op_zoomIn.invokeAsync(self, ((zoom, ), context))

        def begin_zoomIn(self, zoom, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.CCTV._op_zoomIn.begin(self, ((zoom, ), _response, _ex, _sent, context))

        def end_zoomIn(self, _r):
            return _M_Home.CCTV._op_zoomIn.end(self, _r)

        def zoomOut(self, zoom, context=None):
            return _M_Home.CCTV._op_zoomOut.invoke(self, ((zoom, ), context))

        def zoomOutAsync(self, zoom, context=None):
            return _M_Home.CCTV._op_zoomOut.invokeAsync(self, ((zoom, ), context))

        def begin_zoomOut(self, zoom, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.CCTV._op_zoomOut.begin(self, ((zoom, ), _response, _ex, _sent, context))

        def end_zoomOut(self, _r):
            return _M_Home.CCTV._op_zoomOut.end(self, _r)

        def tiltLeft(self, theta, context=None):
            return _M_Home.CCTV._op_tiltLeft.invoke(self, ((theta, ), context))

        def tiltLeftAsync(self, theta, context=None):
            return _M_Home.CCTV._op_tiltLeft.invokeAsync(self, ((theta, ), context))

        def begin_tiltLeft(self, theta, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.CCTV._op_tiltLeft.begin(self, ((theta, ), _response, _ex, _sent, context))

        def end_tiltLeft(self, _r):
            return _M_Home.CCTV._op_tiltLeft.end(self, _r)

        def tiltRight(self, theta, context=None):
            return _M_Home.CCTV._op_tiltRight.invoke(self, ((theta, ), context))

        def tiltRightAsync(self, theta, context=None):
            return _M_Home.CCTV._op_tiltRight.invokeAsync(self, ((theta, ), context))

        def begin_tiltRight(self, theta, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.CCTV._op_tiltRight.begin(self, ((theta, ), _response, _ex, _sent, context))

        def end_tiltRight(self, _r):
            return _M_Home.CCTV._op_tiltRight.end(self, _r)

        def getStatus(self, context=None):
            return _M_Home.CCTV._op_getStatus.invoke(self, ((), context))

        def getStatusAsync(self, context=None):
            return _M_Home.CCTV._op_getStatus.invokeAsync(self, ((), context))

        def begin_getStatus(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.CCTV._op_getStatus.begin(self, ((), _response, _ex, _sent, context))

        def end_getStatus(self, _r):
            return _M_Home.CCTV._op_getStatus.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.CCTVPrx.ice_checkedCast(proxy, '::Home::CCTV', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.CCTVPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::CCTV'
    _M_Home._t_CCTVPrx = IcePy.defineProxy('::Home::CCTV', CCTVPrx)

    _M_Home.CCTVPrx = CCTVPrx
    del CCTVPrx

    _M_Home.CCTV = Ice.createTempClass()
    class CCTV(_M_Home.Device):

        def ice_ids(self, current=None):
            return ('::Home::CCTV', '::Home::Device', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::CCTV'

        @staticmethod
        def ice_staticId():
            return '::Home::CCTV'

        def zoomIn(self, zoom, current=None):
            raise NotImplementedError("servant method 'zoomIn' not implemented")

        def zoomOut(self, zoom, current=None):
            raise NotImplementedError("servant method 'zoomOut' not implemented")

        def tiltLeft(self, theta, current=None):
            raise NotImplementedError("servant method 'tiltLeft' not implemented")

        def tiltRight(self, theta, current=None):
            raise NotImplementedError("servant method 'tiltRight' not implemented")

        def getStatus(self, current=None):
            raise NotImplementedError("servant method 'getStatus' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_CCTVDisp)

        __repr__ = __str__

    _M_Home._t_CCTVDisp = IcePy.defineClass('::Home::CCTV', CCTV, (), None, (_M_Home._t_DeviceDisp,))
    CCTV._ice_type = _M_Home._t_CCTVDisp

    CCTV._op_zoomIn = IcePy.Operation('zoomIn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    CCTV._op_zoomOut = IcePy.Operation('zoomOut', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    CCTV._op_tiltLeft = IcePy.Operation('tiltLeft', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    CCTV._op_tiltRight = IcePy.Operation('tiltRight', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())
    CCTV._op_getStatus = IcePy.Operation('getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Home._t_CCTVStatus, False, 0), ())

    _M_Home.CCTV = CCTV
    del CCTV

if '_t_Readings' not in _M_Home.__dict__:
    _M_Home._t_Readings = IcePy.defineSequence('::Home::Readings', (), IcePy._t_double)

_M_Home._t_Sensor = IcePy.defineValue('::Home::Sensor', Ice.Value, -1, (), False, True, None, ())

if 'SensorPrx' not in _M_Home.__dict__:
    _M_Home.SensorPrx = Ice.createTempClass()
    class SensorPrx(_M_Home.DevicePrx):

        def getLastReading(self, context=None):
            return _M_Home.Sensor._op_getLastReading.invoke(self, ((), context))

        def getLastReadingAsync(self, context=None):
            return _M_Home.Sensor._op_getLastReading.invokeAsync(self, ((), context))

        def begin_getLastReading(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.Sensor._op_getLastReading.begin(self, ((), _response, _ex, _sent, context))

        def end_getLastReading(self, _r):
            return _M_Home.Sensor._op_getLastReading.end(self, _r)

        def getReadings(self, context=None):
            return _M_Home.Sensor._op_getReadings.invoke(self, ((), context))

        def getReadingsAsync(self, context=None):
            return _M_Home.Sensor._op_getReadings.invokeAsync(self, ((), context))

        def begin_getReadings(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Home.Sensor._op_getReadings.begin(self, ((), _response, _ex, _sent, context))

        def end_getReadings(self, _r):
            return _M_Home.Sensor._op_getReadings.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.SensorPrx.ice_checkedCast(proxy, '::Home::Sensor', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.SensorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::Sensor'
    _M_Home._t_SensorPrx = IcePy.defineProxy('::Home::Sensor', SensorPrx)

    _M_Home.SensorPrx = SensorPrx
    del SensorPrx

    _M_Home.Sensor = Ice.createTempClass()
    class Sensor(_M_Home.Device):

        def ice_ids(self, current=None):
            return ('::Home::Device', '::Home::Sensor', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::Sensor'

        @staticmethod
        def ice_staticId():
            return '::Home::Sensor'

        def getLastReading(self, current=None):
            raise NotImplementedError("servant method 'getLastReading' not implemented")

        def getReadings(self, current=None):
            raise NotImplementedError("servant method 'getReadings' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_SensorDisp)

        __repr__ = __str__

    _M_Home._t_SensorDisp = IcePy.defineClass('::Home::Sensor', Sensor, (), None, (_M_Home._t_DeviceDisp,))
    Sensor._ice_type = _M_Home._t_SensorDisp

    Sensor._op_getLastReading = IcePy.Operation('getLastReading', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), (_M_Home._t_NoDataException,))
    Sensor._op_getReadings = IcePy.Operation('getReadings', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Home._t_Readings, False, 0), (_M_Home._t_NoDataException,))

    _M_Home.Sensor = Sensor
    del Sensor

_M_Home._t_LightSensor = IcePy.defineValue('::Home::LightSensor', Ice.Value, -1, (), False, True, None, ())

if 'LightSensorPrx' not in _M_Home.__dict__:
    _M_Home.LightSensorPrx = Ice.createTempClass()
    class LightSensorPrx(_M_Home.SensorPrx):

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.LightSensorPrx.ice_checkedCast(proxy, '::Home::LightSensor', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.LightSensorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::LightSensor'
    _M_Home._t_LightSensorPrx = IcePy.defineProxy('::Home::LightSensor', LightSensorPrx)

    _M_Home.LightSensorPrx = LightSensorPrx
    del LightSensorPrx

    _M_Home.LightSensor = Ice.createTempClass()
    class LightSensor(_M_Home.Sensor):

        def ice_ids(self, current=None):
            return ('::Home::Device', '::Home::LightSensor', '::Home::Sensor', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::LightSensor'

        @staticmethod
        def ice_staticId():
            return '::Home::LightSensor'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_LightSensorDisp)

        __repr__ = __str__

    _M_Home._t_LightSensorDisp = IcePy.defineClass('::Home::LightSensor', LightSensor, (), None, (_M_Home._t_SensorDisp,))
    LightSensor._ice_type = _M_Home._t_LightSensorDisp

    _M_Home.LightSensor = LightSensor
    del LightSensor

_M_Home._t_SoundSensor = IcePy.defineValue('::Home::SoundSensor', Ice.Value, -1, (), False, True, None, ())

if 'SoundSensorPrx' not in _M_Home.__dict__:
    _M_Home.SoundSensorPrx = Ice.createTempClass()
    class SoundSensorPrx(_M_Home.SensorPrx):

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Home.SoundSensorPrx.ice_checkedCast(proxy, '::Home::SoundSensor', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Home.SoundSensorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Home::SoundSensor'
    _M_Home._t_SoundSensorPrx = IcePy.defineProxy('::Home::SoundSensor', SoundSensorPrx)

    _M_Home.SoundSensorPrx = SoundSensorPrx
    del SoundSensorPrx

    _M_Home.SoundSensor = Ice.createTempClass()
    class SoundSensor(_M_Home.Sensor):

        def ice_ids(self, current=None):
            return ('::Home::Device', '::Home::Sensor', '::Home::SoundSensor', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Home::SoundSensor'

        @staticmethod
        def ice_staticId():
            return '::Home::SoundSensor'

        def __str__(self):
            return IcePy.stringify(self, _M_Home._t_SoundSensorDisp)

        __repr__ = __str__

    _M_Home._t_SoundSensorDisp = IcePy.defineClass('::Home::SoundSensor', SoundSensor, (), None, (_M_Home._t_SensorDisp,))
    SoundSensor._ice_type = _M_Home._t_SoundSensorDisp

    _M_Home.SoundSensor = SoundSensor
    del SoundSensor

# End of module Home
