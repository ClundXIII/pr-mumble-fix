# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `FileParser.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__
import IceGrid_Admin_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Start of module IceGrid
__name__ = 'IceGrid'

if not _M_IceGrid.__dict__.has_key('ParseException'):
    _M_IceGrid.ParseException = Ice.createTempClass()
    class ParseException(Ice.UserException):
        '''This exception is raised if an error occurs during parsing.'''
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'IceGrid::ParseException'

    _M_IceGrid._t_ParseException = IcePy.defineException('::IceGrid::ParseException', ParseException, (), None, (('reason', (), IcePy._t_string),))
    ParseException._ice_type = _M_IceGrid._t_ParseException

    _M_IceGrid.ParseException = ParseException
    del ParseException

if not _M_IceGrid.__dict__.has_key('FileParser'):
    _M_IceGrid.FileParser = Ice.createTempClass()
    class FileParser(Ice.Object):
        '''icegridadmin provides a FileParser
object to transform XML files into ApplicationDescriptor
objects.'''
        def __init__(self):
            if __builtin__.type(self) == _M_IceGrid.FileParser:
                raise RuntimeError('IceGrid.FileParser is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::FileParser')

        def ice_id(self, current=None):
            return '::IceGrid::FileParser'

        def ice_staticId():
            return '::IceGrid::FileParser'
        ice_staticId = staticmethod(ice_staticId)

        def parse(self, xmlFile, adminProxy, current=None):
            '''Parse a file.

Arguments:
    xmlFile Full pathname to the file.

    adminProxy An Admin proxy, used only to retrieve default
templates when needed. May be null.

Returns:
     The application descriptor.

Exceptions:
    ParseException Raised if an error occurred during parsing.'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_FileParser)

        __repr__ = __str__

    _M_IceGrid.FileParserPrx = Ice.createTempClass()
    class FileParserPrx(Ice.ObjectPrx):

        '''Parse a file.

Arguments:
    xmlFile Full pathname to the file.

    adminProxy An Admin proxy, used only to retrieve default
templates when needed. May be null.

Returns:
     The application descriptor.

Exceptions:
    ParseException Raised if an error occurred during parsing.'''
        def parse(self, xmlFile, adminProxy, _ctx=None):
            return _M_IceGrid.FileParser._op_parse.invoke(self, ((xmlFile, adminProxy), _ctx))

        '''Parse a file.

Arguments:
    xmlFile Full pathname to the file.

    adminProxy An Admin proxy, used only to retrieve default
templates when needed. May be null.

Returns:
     The application descriptor.

Exceptions:
    ParseException Raised if an error occurred during parsing.'''
        def begin_parse(self, xmlFile, adminProxy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.FileParser._op_parse.begin(self, ((xmlFile, adminProxy), _response, _ex, _sent, _ctx))

        '''Parse a file.

Arguments:
    xmlFile Full pathname to the file.

    adminProxy An Admin proxy, used only to retrieve default
templates when needed. May be null.

Returns:
     The application descriptor.

Exceptions:
    ParseException Raised if an error occurred during parsing.'''
        def end_parse(self, _r):
            return _M_IceGrid.FileParser._op_parse.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.FileParserPrx.ice_checkedCast(proxy, '::IceGrid::FileParser', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.FileParserPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_IceGrid._t_FileParserPrx = IcePy.defineProxy('::IceGrid::FileParser', FileParserPrx)

    _M_IceGrid._t_FileParser = IcePy.defineClass('::IceGrid::FileParser', FileParser, (), True, None, (), ())
    FileParser._ice_type = _M_IceGrid._t_FileParser

    FileParser._op_parse = IcePy.Operation('parse', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), IcePy._t_string), ((), _M_IceGrid._t_AdminPrx)), (), _M_IceGrid._t_ApplicationDescriptor, (_M_IceGrid._t_ParseException,))

    _M_IceGrid.FileParser = FileParser
    del FileParser

    _M_IceGrid.FileParserPrx = FileParserPrx
    del FileParserPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::FileParser"] = "b847ccf3e3db7cbba649ec7cc464faf"
Ice.sliceChecksums["::IceGrid::ParseException"] = "dec9aacba8b3ba76afc5de1cc3489598"
