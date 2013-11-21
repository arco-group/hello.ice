# **********************************************************************
#
# Copyright (c) 2003-2013 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.5.0
#
# <auto-generated>
#
# Generated from file `container.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy

# Start of module Services
_M_Services = Ice.openModule('Services')
__name__ = 'Services'

if 'AlreadyExists' not in _M_Services.__dict__:
    _M_Services.AlreadyExists = Ice.createTempClass()
    class AlreadyExists(Ice.UserException):
        def __init__(self, key=''):
            self.key = key

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Services::AlreadyExists'

    _M_Services._t_AlreadyExists = IcePy.defineException('::Services::AlreadyExists', AlreadyExists, (), False, None, (('key', (), IcePy._t_string, False, 0),))
    AlreadyExists._ice_type = _M_Services._t_AlreadyExists

    _M_Services.AlreadyExists = AlreadyExists
    del AlreadyExists

if 'NoSuchKey' not in _M_Services.__dict__:
    _M_Services.NoSuchKey = Ice.createTempClass()
    class NoSuchKey(Ice.UserException):
        def __init__(self, key=''):
            self.key = key

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'Services::NoSuchKey'

    _M_Services._t_NoSuchKey = IcePy.defineException('::Services::NoSuchKey', NoSuchKey, (), False, None, (('key', (), IcePy._t_string, False, 0),))
    NoSuchKey._ice_type = _M_Services._t_NoSuchKey

    _M_Services.NoSuchKey = NoSuchKey
    del NoSuchKey

if '_t_ProxyMap' not in _M_Services.__dict__:
    _M_Services._t_ProxyMap = IcePy.defineDictionary('::Services::ProxyMap', (), IcePy._t_string, IcePy._t_ObjectPrx)

if 'Container' not in _M_Services.__dict__:
    _M_Services.Container = Ice.createTempClass()
    class Container(Ice.Object):
        def __init__(self):
            if Ice.getType(self) == _M_Services.Container:
                raise RuntimeError('Services.Container is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Services::Container')

        def ice_id(self, current=None):
            return '::Services::Container'

        def ice_staticId():
            return '::Services::Container'
        ice_staticId = staticmethod(ice_staticId)

        def link(self, key, proxy, current=None):
            pass

        def unlink(self, key, current=None):
            pass

        def list(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_Services._t_Container)

        __repr__ = __str__

    _M_Services.ContainerPrx = Ice.createTempClass()
    class ContainerPrx(Ice.ObjectPrx):

        def link(self, key, proxy, _ctx=None):
            return _M_Services.Container._op_link.invoke(self, ((key, proxy), _ctx))

        def begin_link(self, key, proxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Services.Container._op_link.begin(self, ((key, proxy), _response, _ex, _sent, _ctx))

        def end_link(self, _r):
            return _M_Services.Container._op_link.end(self, _r)

        def unlink(self, key, _ctx=None):
            return _M_Services.Container._op_unlink.invoke(self, ((key, ), _ctx))

        def begin_unlink(self, key, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Services.Container._op_unlink.begin(self, ((key, ), _response, _ex, _sent, _ctx))

        def end_unlink(self, _r):
            return _M_Services.Container._op_unlink.end(self, _r)

        def list(self, _ctx=None):
            return _M_Services.Container._op_list.invoke(self, ((), _ctx))

        def begin_list(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_Services.Container._op_list.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_list(self, _r):
            return _M_Services.Container._op_list.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Services.ContainerPrx.ice_checkedCast(proxy, '::Services::Container', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Services.ContainerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Services._t_ContainerPrx = IcePy.defineProxy('::Services::Container', ContainerPrx)

    _M_Services._t_Container = IcePy.defineClass('::Services::Container', Container, -1, (), True, False, None, (), ())
    Container._ice_type = _M_Services._t_Container

    Container._op_link = IcePy.Operation('link', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_ObjectPrx, False, 0)), (), None, (_M_Services._t_AlreadyExists,))
    Container._op_unlink = IcePy.Operation('unlink', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, (_M_Services._t_NoSuchKey,))
    Container._op_list = IcePy.Operation('list', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Services._t_ProxyMap, False, 0), ())

    _M_Services.Container = Container
    del Container

    _M_Services.ContainerPrx = ContainerPrx
    del ContainerPrx

# End of module Services
