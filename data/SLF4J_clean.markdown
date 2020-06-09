# File: `main.java.org.slf4j.ILoggerFactory`

## Package: `main.java.org.slf4j.ILoggerFactory` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.ILoggerFactory` / `public interface ILoggerFactory`

        
        <code>ILoggerFactory</code> instances manufacture {@link Logger}
        instances by name.
        
        <p>Most users retrieve {@link Logger} instances through the static
        {@link LoggerFactory#getLogger(String)} method. An instance of of this
        interface is bound internally with {@link LoggerFactory} class at
        compile time.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `main.java.org.slf4j.ILoggerFactory` / `public Logger getLogger(String name)`

        
        Return an appropriate {@link Logger} instance as specified by the
        <code>name</code> parameter.
        
        <p>If the name parameter is equal to {@link Logger#ROOT_LOGGER_NAME}, that is
        the string value "ROOT" (case insensitive), then the root logger of the
        underlying logging system is returned.
        
        <p>Null-valued name arguments are considered invalid.
        
        <p>Certain extremely simple logging systems, e.g. NOP, may always
        return the same logger instance regardless of the requested name.
        
        @param name the name of the Logger to return
        @return a Logger instance

# File: `main.java.org.slf4j.IMarkerFactory`

## Package: `main.java.org.slf4j.IMarkerFactory` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.IMarkerFactory` / `public interface IMarkerFactory`

        
        Implementations of this interface are used to manufacture {@link Marker}
        instances.
        
        <p>See the section <a href="http://slf4j.org/faq.html#3">Implementing
        the SLF4J API</a> in the FAQ for details on how to make your logging
        system conform to SLF4J.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `main.java.org.slf4j.IMarkerFactory` / `Marker getMarker(String name)`

        
        Manufacture a {@link Marker} instance by name. If the instance has been
        created earlier, return the previously created instance.
        
        <p>Null name values are not allowed.
        
        @param name the name of the marker to be created, null value is
        not allowed.
        
        @return a Marker instance

## Method: `main.java.org.slf4j.IMarkerFactory` / `boolean exists(String name)`

        
        Checks if the marker with the name already exists. If name is null, then false
        is returned.
        
        @param name logger name to check for
        @return true id the marker exists, false otherwise.

## Method: `main.java.org.slf4j.IMarkerFactory` / `boolean detachMarker(String name)`

        
        Detach an existing marker.
        <p>
        Note that after a marker is detached, there might still be "dangling" references
        to the detached marker.
        
        
        @param name The name of the marker to detach
        @return whether the marker  could be detached or not

## Method: `main.java.org.slf4j.IMarkerFactory` / `Marker getDetachedMarker(String name)`

        
        Create a marker which is detached (even at birth) from this IMarkerFactory.
        
        @param name marker name
        @return a dangling marker
        @since 1.5.1

# File: `main.java.org.slf4j.Logger`

## Package: `main.java.org.slf4j.Logger` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.Logger` / `public interface Logger`

        
        The org.slf4j.Logger interface is the main user entry point of SLF4J API.
        It is expected that logging takes place through concrete implementations
        of this interface.
        <p/>
        <h3>Typical usage pattern:</h3>
        <pre>
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        
        public class Wombat {
        
        <span style="color:green">final static Logger logger = LoggerFactory.getLogger(Wombat.class);</span>
        Integer t;
        Integer oldT;
        
        public void setTemperature(Integer temperature) {
        oldT = t;
        t = temperature;
        <span style="color:green">logger.debug("Temperature set to {}. Old temperature was {}.", t, oldT);</span>
        if(temperature.intValue() > 50) {
        <span style="color:green">logger.info("Temperature has risen above 50 degrees.");</span>
        }
        }
        }
        </pre>
        
        Be sure to read the FAQ entry relating to <a href="../../../faq.html#logging_performance">parameterized
        logging</a>. Note that logging statements can be parameterized in
        <a href="../../../faq.html#paramException">presence of an exception/throwable</a>.
        
        <p>Once you are comfortable using loggers, i.e. instances of this interface, consider using
        <a href="MDC.html">MDC</a> as well as <a href="Marker.html">Markers</a>.</p>
        
        @author Ceki G&uuml;lc&uuml;

## Constant: `main.java.org.slf4j.Logger` / `final public String ROOT_LOGGER_NAME`

        
        Case insensitive String constant used to retrieve the name of the root logger.
        
        @since 1.3

## Method: `main.java.org.slf4j.Logger` / `public String getName()`

        
        Return the name of this <code>Logger</code> instance.
        @return name of this logger instance

## Method: `main.java.org.slf4j.Logger` / `public boolean isTraceEnabled()`

        
        Is the logger instance enabled for the TRACE level?
        
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(String msg)`

        
        Log a message at the TRACE level.
        
        @param msg the message string to be logged
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(String format, Object arg)`

        
        Log a message at the TRACE level according to the specified format
        and argument.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the TRACE level. </p>
        
        @param format the format string
        @param arg    the argument
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(String format, Object arg1, Object arg2)`

        
        Log a message at the TRACE level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the TRACE level. </p>
        
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(String format, Object... arguments)`

        
        Log a message at the TRACE level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous string concatenation when the logger
        is disabled for the TRACE level. However, this variant incurs the hidden
        (and relatively small) cost of creating an <code>Object[]</code> before invoking the method,
        even if this logger is disabled for TRACE. The variants taking {@link #trace(String, Object) one} and
        {@link #trace(String, Object, Object) two} arguments exist solely in order to avoid this hidden cost.</p>
        
        @param format    the format string
        @param arguments a list of 3 or more arguments
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(String msg, Throwable t)`

        
        Log an exception (throwable) at the TRACE level with an
        accompanying message.
        
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public boolean isTraceEnabled(Marker marker)`

        
        Similar to {@link #isTraceEnabled()} method except that the
        marker data is also taken into account.
        
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the TRACE level,
        false otherwise.
        
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(Marker marker, String msg)`

        
        Log a message with the specific Marker at the TRACE level.
        
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(Marker marker, String format, Object arg)`

        
        This method is similar to {@link #trace(String, Object)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(Marker marker, String format, Object arg1, Object arg2)`

        
        This method is similar to {@link #trace(String, Object, Object)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(Marker marker, String format, Object... argArray)`

        
        This method is similar to {@link #trace(String, Object...)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker   the marker data specific to this log statement
        @param format   the format string
        @param argArray an array of arguments
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public void trace(Marker marker, String msg, Throwable t)`

        
        This method is similar to {@link #trace(String, Throwable)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log
        @since 1.4

## Method: `main.java.org.slf4j.Logger` / `public boolean isDebugEnabled()`

        
        Is the logger instance enabled for the DEBUG level?
        
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void debug(String msg)`

        
        Log a message at the DEBUG level.
        
        @param msg the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void debug(String format, Object arg)`

        
        Log a message at the DEBUG level according to the specified format
        and argument.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level. </p>
        
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void debug(String format, Object arg1, Object arg2)`

        
        Log a message at the DEBUG level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the DEBUG level. </p>
        
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void debug(String format, Object... arguments)`

        
        Log a message at the DEBUG level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous string concatenation when the logger
        is disabled for the DEBUG level. However, this variant incurs the hidden
        (and relatively small) cost of creating an <code>Object[]</code> before invoking the method,
        even if this logger is disabled for DEBUG. The variants taking
        {@link #debug(String, Object) one} and {@link #debug(String, Object, Object) two}
        arguments exist solely in order to avoid this hidden cost.</p>
        
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void debug(String msg, Throwable t)`

        
        Log an exception (throwable) at the DEBUG level with an
        accompanying message.
        
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isDebugEnabled(Marker marker)`

        
        Similar to {@link #isDebugEnabled()} method except that the
        marker data is also taken into account.
        
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the DEBUG level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void debug(Marker marker, String msg)`

        
        Log a message with the specific Marker at the DEBUG level.
        
        @param marker the marker data specific to this log statement
        @param msg    the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void debug(Marker marker, String format, Object arg)`

        
        This method is similar to {@link #debug(String, Object)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void debug(Marker marker, String format, Object arg1, Object arg2)`

        
        This method is similar to {@link #debug(String, Object, Object)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void debug(Marker marker, String format, Object... arguments)`

        
        This method is similar to {@link #debug(String, Object...)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void debug(Marker marker, String msg, Throwable t)`

        
        This method is similar to {@link #debug(String, Throwable)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isInfoEnabled()`

        
        Is the logger instance enabled for the INFO level?
        
        @return True if this Logger is enabled for the INFO level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void info(String msg)`

        
        Log a message at the INFO level.
        
        @param msg the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void info(String format, Object arg)`

        
        Log a message at the INFO level according to the specified format
        and argument.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the INFO level. </p>
        
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void info(String format, Object arg1, Object arg2)`

        
        Log a message at the INFO level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the INFO level. </p>
        
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void info(String format, Object... arguments)`

        
        Log a message at the INFO level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous string concatenation when the logger
        is disabled for the INFO level. However, this variant incurs the hidden
        (and relatively small) cost of creating an <code>Object[]</code> before invoking the method,
        even if this logger is disabled for INFO. The variants taking
        {@link #info(String, Object) one} and {@link #info(String, Object, Object) two}
        arguments exist solely in order to avoid this hidden cost.</p>
        
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void info(String msg, Throwable t)`

        
        Log an exception (throwable) at the INFO level with an
        accompanying message.
        
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isInfoEnabled(Marker marker)`

        
        Similar to {@link #isInfoEnabled()} method except that the marker
        data is also taken into consideration.
        
        @param marker The marker data to take into consideration
        @return true if this logger is warn enabled, false otherwise

## Method: `main.java.org.slf4j.Logger` / `public void info(Marker marker, String msg)`

        
        Log a message with the specific Marker at the INFO level.
        
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void info(Marker marker, String format, Object arg)`

        
        This method is similar to {@link #info(String, Object)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void info(Marker marker, String format, Object arg1, Object arg2)`

        
        This method is similar to {@link #info(String, Object, Object)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void info(Marker marker, String format, Object... arguments)`

        
        This method is similar to {@link #info(String, Object...)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void info(Marker marker, String msg, Throwable t)`

        
        This method is similar to {@link #info(String, Throwable)} method
        except that the marker data is also taken into consideration.
        
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isWarnEnabled()`

        
        Is the logger instance enabled for the WARN level?
        
        @return True if this Logger is enabled for the WARN level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void warn(String msg)`

        
        Log a message at the WARN level.
        
        @param msg the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void warn(String format, Object arg)`

        
        Log a message at the WARN level according to the specified format
        and argument.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the WARN level. </p>
        
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void warn(String format, Object... arguments)`

        
        Log a message at the WARN level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous string concatenation when the logger
        is disabled for the WARN level. However, this variant incurs the hidden
        (and relatively small) cost of creating an <code>Object[]</code> before invoking the method,
        even if this logger is disabled for WARN. The variants taking
        {@link #warn(String, Object) one} and {@link #warn(String, Object, Object) two}
        arguments exist solely in order to avoid this hidden cost.</p>
        
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void warn(String format, Object arg1, Object arg2)`

        
        Log a message at the WARN level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the WARN level. </p>
        
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void warn(String msg, Throwable t)`

        
        Log an exception (throwable) at the WARN level with an
        accompanying message.
        
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isWarnEnabled(Marker marker)`

        
        Similar to {@link #isWarnEnabled()} method except that the marker
        data is also taken into consideration.
        
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the WARN level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void warn(Marker marker, String msg)`

        
        Log a message with the specific Marker at the WARN level.
        
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void warn(Marker marker, String format, Object arg)`

        
        This method is similar to {@link #warn(String, Object)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void warn(Marker marker, String format, Object arg1, Object arg2)`

        
        This method is similar to {@link #warn(String, Object, Object)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void warn(Marker marker, String format, Object... arguments)`

        
        This method is similar to {@link #warn(String, Object...)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void warn(Marker marker, String msg, Throwable t)`

        
        This method is similar to {@link #warn(String, Throwable)} method
        except that the marker data is also taken into consideration.
        
        @param marker the marker data for this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isErrorEnabled()`

        
        Is the logger instance enabled for the ERROR level?
        
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void error(String msg)`

        
        Log a message at the ERROR level.
        
        @param msg the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void error(String format, Object arg)`

        
        Log a message at the ERROR level according to the specified format
        and argument.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the ERROR level. </p>
        
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void error(String format, Object arg1, Object arg2)`

        
        Log a message at the ERROR level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous object creation when the logger
        is disabled for the ERROR level. </p>
        
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void error(String format, Object... arguments)`

        
        Log a message at the ERROR level according to the specified format
        and arguments.
        <p/>
        <p>This form avoids superfluous string concatenation when the logger
        is disabled for the ERROR level. However, this variant incurs the hidden
        (and relatively small) cost of creating an <code>Object[]</code> before invoking the method,
        even if this logger is disabled for ERROR. The variants taking
        {@link #error(String, Object) one} and {@link #error(String, Object, Object) two}
        arguments exist solely in order to avoid this hidden cost.</p>
        
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void error(String msg, Throwable t)`

        
        Log an exception (throwable) at the ERROR level with an
        accompanying message.
        
        @param msg the message accompanying the exception
        @param t   the exception (throwable) to log

## Method: `main.java.org.slf4j.Logger` / `public boolean isErrorEnabled(Marker marker)`

        
        Similar to {@link #isErrorEnabled()} method except that the
        marker data is also taken into consideration.
        
        @param marker The marker data to take into consideration
        @return True if this Logger is enabled for the ERROR level,
        false otherwise.

## Method: `main.java.org.slf4j.Logger` / `public void error(Marker marker, String msg)`

        
        Log a message with the specific Marker at the ERROR level.
        
        @param marker The marker specific to this log statement
        @param msg    the message string to be logged

## Method: `main.java.org.slf4j.Logger` / `public void error(Marker marker, String format, Object arg)`

        
        This method is similar to {@link #error(String, Object)} method except that the
        marker data is also taken into consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg    the argument

## Method: `main.java.org.slf4j.Logger` / `public void error(Marker marker, String format, Object arg1, Object arg2)`

        
        This method is similar to {@link #error(String, Object, Object)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param format the format string
        @param arg1   the first argument
        @param arg2   the second argument

## Method: `main.java.org.slf4j.Logger` / `public void error(Marker marker, String format, Object... arguments)`

        
        This method is similar to {@link #error(String, Object...)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker    the marker data specific to this log statement
        @param format    the format string
        @param arguments a list of 3 or more arguments

## Method: `main.java.org.slf4j.Logger` / `public void error(Marker marker, String msg, Throwable t)`

        
        This method is similar to {@link #error(String, Throwable)}
        method except that the marker data is also taken into
        consideration.
        
        @param marker the marker data specific to this log statement
        @param msg    the message accompanying the exception
        @param t      the exception (throwable) to log

# File: `main.java.org.slf4j.LoggerFactory`

## Package: `main.java.org.slf4j.LoggerFactory` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.LoggerFactory` / `public final class LoggerFactory`

        
        The <code>LoggerFactory</code> is a utility class producing Loggers for
        various logging APIs, most notably for log4j, logback and JDK 1.4 logging.
        Other implementations such as {@link org.slf4j.impl.NOPLogger NOPLogger} and
        {@link org.slf4j.impl.SimpleLogger SimpleLogger} are also supported.
        <p/>
        <p/>
        <code>LoggerFactory</code> is essentially a wrapper around an
        {@link ILoggerFactory} instance bound with <code>LoggerFactory</code> at
        compile time.
        <p/>
        <p/>
        Please note that all methods in <code>LoggerFactory</code> are static.
        
        
        @author Alexander Dorokhine
        @author Robert Elliot
        @author Ceki G&uuml;lc&uuml;

## Field: `main.java.org.slf4j.LoggerFactory` / `static private final String[] API_COMPATIBILITY_LIST`

        
        It is LoggerFactory's responsibility to track version changes and manage
        the compatibility list.
        <p/>
        <p/>
        It is assumed that all versions in the 1.6 are mutually compatible.

## Method: `main.java.org.slf4j.LoggerFactory` / `static void reset()`

        
        Force LoggerFactory to consider itself uninitialized.
        <p/>
        <p/>
        This method is intended to be called by classes (in the same package) for
        testing purposes. This method is internal. It can be modified, renamed or
        removed at any time without notice.
        <p/>
        <p/>
        You are strongly discouraged from calling this method in production code.

## Method: `main.java.org.slf4j.LoggerFactory` / `private static void reportMultipleBindingAmbiguity(Set<URL> binderPathSet)`

        
        Prints a warning message on the console if multiple bindings were found on the class path.
        No reporting is done otherwise.

## Method: `main.java.org.slf4j.LoggerFactory` / `public static Logger getLogger(String name)`

        
        Return a logger named according to the name parameter using the statically
        bound {@link ILoggerFactory} instance.
        
        @param name The name of the logger.
        @return logger

## Method: `main.java.org.slf4j.LoggerFactory` / `public static Logger getLogger(Class<?> clazz)`

        
        Return a logger named corresponding to the class passed as parameter, using
        the statically bound {@link ILoggerFactory} instance.
        
        <p>In case the the <code>clazz</code> parameter differs from the name of
        the caller as computed internally by SLF4J, a logger name mismatch warning will be
        printed but only if the <code>slf4j.detectLoggerNameMismatch</code> system property is
        set to true. By default, this property is not set and no warnings will be printed
        even in case of a logger name mismatch.
        
        @param clazz the returned logger will be named after clazz
        @return logger
        
        
        @see <a href="http://www.slf4j.org/codes.html#loggerNameMismatch">Detected logger name mismatch</a>

## Method: `main.java.org.slf4j.LoggerFactory` / `public static ILoggerFactory getILoggerFactory()`

        
        Return the {@link ILoggerFactory} instance in use.
        <p/>
        <p/>
        ILoggerFactory instance is bound with this class at compile time.
        
        @return the ILoggerFactory instance in use

# File: `main.java.org.slf4j.MDC`

## Package: `main.java.org.slf4j.MDC` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.MDC` / `public class MDC`

        
        This class hides and serves as a substitute for the underlying logging
        system's MDC implementation.
        
        <p>
        If the underlying logging system offers MDC functionality, then SLF4J's MDC,
        i.e. this class, will delegate to the underlying system's MDC. Note that at
        this time, only two logging systems, namely log4j and logback, offer MDC
        functionality. For java.util.logging which does not support MDC,
        {@link BasicMDCAdapter} will be used. For other systems, i.e slf4j-simple
        and slf4j-nop, {@link NOPMDCAdapter} will be used.
        
        <p>
        Thus, as a SLF4J user, you can take advantage of MDC in the presence of log4j,
        logback, or java.util.logging, but without forcing these systems as
        dependencies upon your users.
        
        <p>
        For more information on MDC please see the <a
        href="http://logback.qos.ch/manual/mdc.html">chapter on MDC</a> in the
        logback manual.
        
        <p>
        Please note that all methods in this class are static.
        
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1

## Class: `main.java.org.slf4j.MDC` / `public static class MDCCloseable implements Closeable`

        
        An adapter to remove the key when done.

## Method: `main.java.org.slf4j.MDC` / `private static MDCAdapter bwCompatibleGetMDCAdapterFromBinder() throws NoClassDefFoundError`

        
        As of SLF4J version 1.7.14, StaticMDCBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        
        @return MDCAdapter
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14

## Method: `main.java.org.slf4j.MDC` / `public static void put(String key, String val) throws IllegalArgumentException`

        
        Put a diagnostic context value (the <code>val</code> parameter) as identified with the
        <code>key</code> parameter into the current thread's diagnostic context map. The
        <code>key</code> parameter cannot be null. The <code>val</code> parameter
        can be null only if the underlying implementation supports it.
        
        <p>
        This method delegates all work to the MDC of the underlying logging system.
        
        @param key non-null key
        @param val value to put in the map
        
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `main.java.org.slf4j.MDC` / `public static MDCCloseable putCloseable(String key, String val) throws IllegalArgumentException`

        
        Put a diagnostic context value (the <code>val</code> parameter) as identified with the
        <code>key</code> parameter into the current thread's diagnostic context map. The
        <code>key</code> parameter cannot be null. The <code>val</code> parameter
        can be null only if the underlying implementation supports it.
        
        <p>
        This method delegates all work to the MDC of the underlying logging system.
        <p>
        This method return a <code>Closeable</code> object who can remove <code>key</code> when
        <code>close</code> is called.
        
        <p>
        Useful with Java 7 for example :
        <code>
        try(MDC.MDCCloseable closeable = MDC.putCloseable(key, value)) {
        ....
        }
        </code>
        
        @param key non-null key
        @param val value to put in the map
        @return a <code>Closeable</code> who can remove <code>key</code> when <code>close</code>
        is called.
        
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `main.java.org.slf4j.MDC` / `public static String get(String key) throws IllegalArgumentException`

        
        Get the diagnostic context identified by the <code>key</code> parameter. The
        <code>key</code> parameter cannot be null.
        
        <p>
        This method delegates all work to the MDC of the underlying logging system.
        
        @param key
        @return the string value identified by the <code>key</code> parameter.
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `main.java.org.slf4j.MDC` / `public static void remove(String key) throws IllegalArgumentException`

        
        Remove the diagnostic context identified by the <code>key</code> parameter using
        the underlying system's MDC implementation. The <code>key</code> parameter
        cannot be null. This method does nothing if there is no previous value
        associated with <code>key</code>.
        
        @param key
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `main.java.org.slf4j.MDC` / `public static void clear()`

        
        Clear all entries in the MDC of the underlying implementation.

## Method: `main.java.org.slf4j.MDC` / `public static Map<String, String> getCopyOfContextMap()`

        
        Return a copy of the current thread's context map, with keys and values of
        type String. Returned value may be null.
        
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1

## Method: `main.java.org.slf4j.MDC` / `public static void setContextMap(Map<String, String> contextMap)`

        
        Set the current thread's context map by first clearing any existing map and
        then copying the map passed as parameter. The context map passed as
        parameter must only contain keys and values of type String.
        
        @param contextMap
        must contain only keys and values of type String
        @since 1.5.1

## Method: `main.java.org.slf4j.MDC` / `public static MDCAdapter getMDCAdapter()`

        
        Returns the MDCAdapter instance currently in use.
        
        @return the MDcAdapter instance currently in use.
        @since 1.4.2

# File: `main.java.org.slf4j.Marker`

## Package: `main.java.org.slf4j.Marker` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.Marker` / `public interface Marker extends Serializable`

        
        Markers are named objects used to enrich log statements. Conforming logging
        system Implementations of SLF4J determine how information conveyed by markers
        are used, if at all. In particular, many conforming logging systems ignore
        marker data.
        
        <p>
        Markers can contain references to other markers, which in turn may contain
        references of their own.
        
        @author Ceki G&uuml;lc&uuml;

## Constant: `main.java.org.slf4j.Marker` / `public final String ANY_MARKER`

        
        This constant represents any marker, including a null marker.

## Constant: `main.java.org.slf4j.Marker` / `public final String ANY_NON_NULL_MARKER`

        
        This constant represents any non-null marker.

## Method: `main.java.org.slf4j.Marker` / `public String getName()`

        
        Get the name of this Marker.
        
        @return name of marker

## Method: `main.java.org.slf4j.Marker` / `public void add(Marker reference)`

        
        Add a reference to another Marker.
        
        @param reference
        a reference to another marker
        @throws IllegalArgumentException
        if 'reference' is null

## Method: `main.java.org.slf4j.Marker` / `public boolean remove(Marker reference)`

        
        Remove a marker reference.
        
        @param reference
        the marker reference to remove
        @return true if reference could be found and removed, false otherwise.

## Method: `main.java.org.slf4j.Marker` / `public boolean hasChildren()`

        
        @deprecated Replaced by {@link #hasReferences()}.

## Method: `main.java.org.slf4j.Marker` / `public boolean hasReferences()`

        
        Does this marker have any references?
        
        @return true if this marker has one or more references, false otherwise.

## Method: `main.java.org.slf4j.Marker` / `public Iterator<Marker> iterator()`

        
        Returns an Iterator which can be used to iterate over the references of this
        marker. An empty iterator is returned when this marker has no references.
        
        @return Iterator over the references of this marker

## Method: `main.java.org.slf4j.Marker` / `public boolean contains(Marker other)`

        
        Does this marker contain a reference to the 'other' marker? Marker A is defined
        to contain marker B, if A == B or if B is referenced by A, or if B is referenced
        by any one of A's references (recursively).
        
        @param other
        The marker to test for inclusion.
        @throws IllegalArgumentException
        if 'other' is null
        @return Whether this marker contains the other marker.

## Method: `main.java.org.slf4j.Marker` / `public boolean contains(String name)`

        
        Does this marker contain the marker named 'name'?
        
        If 'name' is null the returned value is always false.
        
        @param name The marker name to test for inclusion.
        @return Whether this marker contains the other marker.

## Method: `main.java.org.slf4j.Marker` / `public boolean equals(Object o)`

        
        Markers are considered equal if they have the same name.
        
        @param o
        @return true, if this.name equals o.name
        
        @since 1.5.1

## Method: `main.java.org.slf4j.Marker` / `public int hashCode()`

        
        Compute the hash code based on the name of this marker.
        Note that markers are considered equal if they have the same name.
        
        @return the computed hashCode
        @since 1.5.1

# File: `main.java.org.slf4j.MarkerFactory`

## Package: `main.java.org.slf4j.MarkerFactory` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.MarkerFactory` / `public class MarkerFactory`

        
        MarkerFactory is a utility class producing {@link Marker} instances as
        appropriate for the logging system currently in use.
        
        <p>
        This class is essentially implemented as a wrapper around an
        {@link IMarkerFactory} instance bound at compile time.
        
        <p>
        Please note that all methods in this class are static.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `main.java.org.slf4j.MarkerFactory` / `private static IMarkerFactory bwCompatibleGetMarkerFactoryFromBinder() throws NoClassDefFoundError`

        
        As of SLF4J version 1.7.14, StaticMarkerBinder classes shipping in various bindings
        come with a getSingleton() method. Previously only a public field called SINGLETON
        was available.
        
        @return IMarkerFactory
        @throws NoClassDefFoundError in case no binding is available
        @since 1.7.14

## Method: `main.java.org.slf4j.MarkerFactory` / `public static Marker getMarker(String name)`

        
        Return a Marker instance as specified by the name parameter using the
        previously bound {@link IMarkerFactory}instance.
        
        @param name
        The name of the {@link Marker} object to return.
        @return marker

## Method: `main.java.org.slf4j.MarkerFactory` / `public static Marker getDetachedMarker(String name)`

        
        Create a marker which is detached (even at birth) from the MarkerFactory.
        
        @param name the name of the marker
        @return a dangling marker
        @since 1.5.1

## Method: `main.java.org.slf4j.MarkerFactory` / `public static IMarkerFactory getIMarkerFactory()`

        
        Return the {@link IMarkerFactory}instance in use.
        
        <p>The IMarkerFactory instance is usually bound with this class at
        compile time.
        
        @return the IMarkerFactory instance in use

# File: `main.java.org.slf4j.event.EventConstants`

# File: `main.java.org.slf4j.event.EventRecodingLogger`

# File: `main.java.org.slf4j.event.Level`

## Enum: `main.java.org.slf4j.event.Level` / `public enum Level`

        
        
        @author ceki
        @since 1.7.15

## Method: `main.java.org.slf4j.event.Level` / `public String toString()`

        
        Returns the string representation of this Level.

# File: `main.java.org.slf4j.event.LoggingEvent`

## Interface: `main.java.org.slf4j.event.LoggingEvent` / `public interface LoggingEvent`

        
        
        @author ceki
        @since 1.7.15

# File: `main.java.org.slf4j.event.SubstituteLoggingEvent`

# File: `main.java.org.slf4j.helpers.BasicMDCAdapter`

## Package: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public class BasicMDCAdapter implements MDCAdapter`

        
        Basic MDC implementation, which can be used with logging systems that lack
        out-of-the-box MDC support.
        
        This code was initially inspired by  logback's LogbackMDCAdapter. However,
        LogbackMDCAdapter has evolved and is now considerably more sophisticated.
        
        @author Ceki Gulcu
        @author Maarten Bosteels
        @author Lukasz Cwik
        
        @since 1.5.0

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public void put(String key, String val)`

        
        Put a context value (the <code>val</code> parameter) as identified with
        the <code>key</code> parameter into the current thread's context map.
        Note that contrary to log4j, the <code>val</code> parameter can be null.
        
        <p>
        If the current thread does not have a context map it is created as a side
        effect of this call.
        
        @throws IllegalArgumentException
        in case the "key" parameter is null

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public String get(String key)`

        
        Get the context identified by the <code>key</code> parameter.

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public void remove(String key)`

        
        Remove the the context identified by the <code>key</code> parameter.

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public void clear()`

        
        Clear all entries in the MDC.

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public Set<String> getKeys()`

        
        Returns the keys in the MDC as a {@link Set} of {@link String}s The
        returned value can be null.
        
        @return the keys in the MDC

## Method: `main.java.org.slf4j.helpers.BasicMDCAdapter` / `public Map<String, String> getCopyOfContextMap()`

        
        Return a copy of the current thread's context map.
        Returned value may be null.

# File: `main.java.org.slf4j.helpers.BasicMarker`

## Package: `main.java.org.slf4j.helpers.BasicMarker` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.BasicMarker` / `public class BasicMarker implements Marker`

        
        A simple implementation of the {@link Marker} interface.
        
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn

## Method: `main.java.org.slf4j.helpers.BasicMarker` / `public boolean contains(String name)`

        
        This method is mainly used with Expression Evaluators.

# File: `main.java.org.slf4j.helpers.BasicMarkerFactory`

## Package: `main.java.org.slf4j.helpers.BasicMarkerFactory` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.BasicMarkerFactory` / `public class BasicMarkerFactory implements IMarkerFactory`

        
        An almost trivial implementation of the {@link IMarkerFactory}
        interface which creates {@link BasicMarker} instances.
        
        <p>Simple logging systems can conform to the SLF4J API by binding
        {@link org.slf4j.MarkerFactory} with an instance of this class.
        
        @author Ceki G&uuml;lc&uuml;

## Constructor: `main.java.org.slf4j.helpers.BasicMarkerFactory` / `public BasicMarkerFactory()`

        
        Regular users should <em>not</em> create
        <code>BasicMarkerFactory</code> instances. <code>Marker</code>
        instances can be obtained using the static {@link
        org.slf4j.MarkerFactory#getMarker} method.

## Method: `main.java.org.slf4j.helpers.BasicMarkerFactory` / `public Marker getMarker(String name)`

        
        Manufacture a {@link BasicMarker} instance by name. If the instance has been
        created earlier, return the previously created instance.
        
        @param name the name of the marker to be created
        @return a Marker instance

## Method: `main.java.org.slf4j.helpers.BasicMarkerFactory` / `public boolean exists(String name)`

        
        Does the name marked already exist?

# File: `main.java.org.slf4j.helpers.FormattingTuple`

## Package: `main.java.org.slf4j.helpers.FormattingTuple` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.FormattingTuple` / `public class FormattingTuple`

        
        Holds the results of formatting done by {@link MessageFormatter}.
        
        @author Joern Huxhorn

# File: `main.java.org.slf4j.helpers.MarkerIgnoringBase`

## Package: `main.java.org.slf4j.helpers.MarkerIgnoringBase` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.MarkerIgnoringBase` / `public abstract class MarkerIgnoringBase extends NamedLoggerBase implements Logger`

        
        This class serves as base for adapters or native implementations of logging systems
        lacking Marker support. In this implementation, methods taking marker data
        simply invoke the corresponding method without the Marker argument, discarding
        any marker data passed as argument.
        
        @author Ceki Gulcu

# File: `main.java.org.slf4j.helpers.MessageFormatter`

## Package: `main.java.org.slf4j.helpers.MessageFormatter` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.MessageFormatter` / `final public class MessageFormatter`

        
        Formats messages according to very simple substitution rules. Substitutions
        can be made 1, 2 or more arguments.
        
        <p>
        For example,
        
        <pre>
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;)
        </pre>
        
        will return the string "Hi there.".
        <p>
        The {} pair is called the <em>formatting anchor</em>. It serves to designate
        the location where arguments need to be substituted within the message
        pattern.
        <p>
        In case your message contains the '{' or the '}' character, you do not have
        to do anything special unless the '}' character immediately follows '{'. For
        example,
        
        <pre>
        MessageFormatter.format(&quot;Set {1,2,3} is not equal to {}.&quot;, &quot;1,2&quot;);
        </pre>
        
        will return the string "Set {1,2,3} is not equal to 1,2.".
        
        <p>
        If for whatever reason you need to place the string "{}" in the message
        without its <em>formatting anchor</em> meaning, then you need to escape the
        '{' character with '\', that is the backslash character. Only the '{'
        character should be escaped. There is no need to escape the '}' character.
        For example,
        
        <pre>
        MessageFormatter.format(&quot;Set \\{} is not equal to {}.&quot;, &quot;1,2&quot;);
        </pre>
        
        will return the string "Set {} is not equal to 1,2.".
        
        <p>
        The escaping behavior just described can be overridden by escaping the escape
        character '\'. Calling
        
        <pre>
        MessageFormatter.format(&quot;File name is C:\\\\{}.&quot;, &quot;file.zip&quot;);
        </pre>
        
        will return the string "File name is C:\file.zip".
        
        <p>
        The formatting conventions are different than those of {@link MessageFormat}
        which ships with the Java platform. This is justified by the fact that
        SLF4J's implementation is 10 times faster than that of {@link MessageFormat}.
        This local performance difference is both measurable and significant in the
        larger context of the complete logging processing chain.
        
        <p>
        See also {@link #format(String, Object)},
        {@link #format(String, Object, Object)} and
        {@link #arrayFormat(String, Object[])} methods for more details.
        
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn

## Method: `main.java.org.slf4j.helpers.MessageFormatter` / `final public static FormattingTuple format(String messagePattern, Object arg)`

        
        Performs single argument substitution for the 'messagePattern' passed as
        parameter.
        <p>
        For example,
        
        <pre>
        MessageFormatter.format(&quot;Hi {}.&quot;, &quot;there&quot;);
        </pre>
        
        will return the string "Hi there.".
        <p>
        
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg
        The argument to be substituted in place of the formatting anchor
        @return The formatted message

## Method: `main.java.org.slf4j.helpers.MessageFormatter` / `final public static FormattingTuple format(final String messagePattern, Object arg1, Object arg2)`

        
        
        Performs a two argument substitution for the 'messagePattern' passed as
        parameter.
        <p>
        For example,
        
        <pre>
        MessageFormatter.format(&quot;Hi {}. My name is {}.&quot;, &quot;Alice&quot;, &quot;Bob&quot;);
        </pre>
        
        will return the string "Hi Alice. My name is Bob.".
        
        @param messagePattern
        The message pattern which will be parsed and formatted
        @param arg1
        The argument to be substituted in place of the first formatting
        anchor
        @param arg2
        The argument to be substituted in place of the second formatting
        anchor
        @return The formatted message

# File: `main.java.org.slf4j.helpers.NOPLogger`

## Package: `main.java.org.slf4j.helpers.NOPLogger` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.NOPLogger` / `public class NOPLogger extends MarkerIgnoringBase`

        
        A direct NOP (no operation) implementation of {@link Logger}.
        
        @author Ceki G&uuml;lc&uuml;

## Field: `main.java.org.slf4j.helpers.NOPLogger` / `public static final NOPLogger NOP_LOGGER`

        
        The unique instance of NOPLogger.

## Constructor: `main.java.org.slf4j.helpers.NOPLogger` / `protected NOPLogger()`

        
        There is no point in creating multiple instances of NOPLOgger,
        except by derived classes, hence the protected  access for the constructor.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public String getName()`

        
        Always returns the string value "NOP".

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public boolean isTraceEnabled()`

        
        Always returns false.
        @return always false

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void trace(String msg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void trace(String format, Object arg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void trace(String format, Object arg1, Object arg2)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void trace(String format, Object... argArray)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void trace(String msg, Throwable t)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public boolean isDebugEnabled()`

        
        Always returns false.
        @return always false

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void debug(String msg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void debug(String format, Object arg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void debug(String format, Object arg1, Object arg2)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void debug(String format, Object... argArray)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void debug(String msg, Throwable t)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public boolean isInfoEnabled()`

        
        Always returns false.
        @return always false

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void info(String msg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void info(String format, Object arg1)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void info(String format, Object arg1, Object arg2)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void info(String format, Object... argArray)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void info(String msg, Throwable t)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public boolean isWarnEnabled()`

        
        Always returns false.
        @return always false

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void warn(String msg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void warn(String format, Object arg1)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void warn(String format, Object arg1, Object arg2)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void warn(String format, Object... argArray)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void warn(String msg, Throwable t)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public boolean isErrorEnabled()`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void error(String msg)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void error(String format, Object arg1)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void error(String format, Object arg1, Object arg2)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `public final void error(String format, Object... argArray)`

        A NOP implementation.

## Method: `main.java.org.slf4j.helpers.NOPLogger` / `final public void error(String msg, Throwable t)`

        A NOP implementation.

# File: `main.java.org.slf4j.helpers.NOPLoggerFactory`

## Package: `main.java.org.slf4j.helpers.NOPLoggerFactory` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.NOPLoggerFactory` / `public class NOPLoggerFactory implements ILoggerFactory`

        
        NOPLoggerFactory is an trivial implementation of {@link
        ILoggerFactory} which always returns the unique instance of
        NOPLogger.
        
        @author Ceki G&uuml;lc&uuml;

# File: `main.java.org.slf4j.helpers.NOPMDCAdapter`

## Package: `main.java.org.slf4j.helpers.NOPMDCAdapter` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.NOPMDCAdapter` / `public class NOPMDCAdapter implements MDCAdapter`

        
        This adapter is an empty implementation of the {@link MDCAdapter} interface.
        It is used for all logging systems which do not support mapped
        diagnostic contexts such as JDK14, simple and NOP.
        
        @author Ceki G&uuml;lc&uuml;
        
        @since 1.4.1

# File: `main.java.org.slf4j.helpers.NamedLoggerBase`

## Package: `main.java.org.slf4j.helpers.NamedLoggerBase` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.NamedLoggerBase` / `abstract class NamedLoggerBase implements Logger, Serializable`

        
        Serves as base class for named logger implementation. More significantly, this
        class establishes deserialization behavior. See @see #readResolve.
        
        @author Ceki Gulcu
        @since 1.5.3

## Method: `main.java.org.slf4j.helpers.NamedLoggerBase` / `protected Object readResolve() throws ObjectStreamException`

        
        Replace this instance with a homonymous (same name) logger returned
        by LoggerFactory. Note that this method is only called during
        deserialization.
        
        <p>
        This approach will work well if the desired ILoggerFactory is the one
        references by LoggerFactory. However, if the user manages its logger hierarchy
        through a different (non-static) mechanism, e.g. dependency injection, then
        this approach would be mostly counterproductive.
        
        @return logger with same name as returned by LoggerFactory
        @throws ObjectStreamException

# File: `main.java.org.slf4j.helpers.SubstituteLogger`

## Package: `main.java.org.slf4j.helpers.SubstituteLogger` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.SubstituteLogger` / `public class SubstituteLogger implements Logger`

        
        A logger implementation which logs via a delegate logger. By default, the delegate is a
        {@link NOPLogger}. However, a different delegate can be set at any time.
        <p/>
        See also the <a href="http://www.slf4j.org/codes.html#substituteLogger">relevant
        error code</a> documentation.
        
        @author Chetan Mehrotra
        @author Ceki Gulcu

## Method: `main.java.org.slf4j.helpers.SubstituteLogger` / `Logger delegate()`

        
        Return the delegate logger instance if set. Otherwise, return a {@link NOPLogger}
        instance.

## Method: `main.java.org.slf4j.helpers.SubstituteLogger` / `public void setDelegate(Logger delegate)`

        
        Typically called after the {@link org.slf4j.LoggerFactory} initialization phase is completed.
        @param delegate

# File: `main.java.org.slf4j.helpers.SubstituteLoggerFactory`

## Package: `main.java.org.slf4j.helpers.SubstituteLoggerFactory` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.SubstituteLoggerFactory` / `public class SubstituteLoggerFactory implements ILoggerFactory`

        
        SubstituteLoggerFactory manages instances of {@link SubstituteLogger}.
        
        @author Ceki G&uuml;lc&uuml;
        @author Chetan Mehrotra

# File: `main.java.org.slf4j.helpers.Util`

## Package: `main.java.org.slf4j.helpers.Util` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.helpers.Util` / `public final class Util`

        
        An internal utility class.
        
        @author Alexander Dorokhine
        @author Ceki G&uuml;lc&uuml;

## Class: `main.java.org.slf4j.helpers.Util` / `private static final class ClassContextSecurityManager extends SecurityManager`

        
        In order to call {@link SecurityManager#getClassContext()}, which is a
        protected method, we add this wrapper which allows the method to be visible
        inside this package.

## Method: `main.java.org.slf4j.helpers.Util` / `public static Class<?> getCallingClass()`

        
        Returns the name of the class which called the invoking method.
        
        @return the name of the class which called the invoking method.

# File: `main.java.org.slf4j.impl.StaticLoggerBinder`

## Package: `main.java.org.slf4j.impl.StaticLoggerBinder` / `package org.slf4j.impl`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.impl.StaticLoggerBinder` / `public class StaticLoggerBinder`

        
        The binding of {@link org.slf4j.LoggerFactory} class with an actual instance of
        {@link ILoggerFactory} is performed using information returned by this class.
        
        This class is meant to provide a dummy StaticLoggerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-log4j12 etc.
        
        @author Ceki G&uuml;lc&uuml;

## Field: `main.java.org.slf4j.impl.StaticLoggerBinder` / `private static final StaticLoggerBinder SINGLETON`

        
        The unique instance of this class.

## Method: `main.java.org.slf4j.impl.StaticLoggerBinder` / `public static final StaticLoggerBinder getSingleton()`

        
        Return the singleton of this class.
        
        @return the StaticLoggerBinder singleton

## Field: `main.java.org.slf4j.impl.StaticLoggerBinder` / `public static String REQUESTED_API_VERSION`

        
        Declare the version of the SLF4J API this implementation is compiled against.
        The value of this field is modified with each major release.

# File: `main.java.org.slf4j.impl.StaticMDCBinder`

## Package: `main.java.org.slf4j.impl.StaticMDCBinder` / `package org.slf4j.impl`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.impl.StaticMDCBinder` / `public class StaticMDCBinder`

        
        This class is only a stub. Real implementations are found in
        each SLF4J binding project, e.g. slf4j-nop, slf4j-log4j12 etc.
        
        @author Ceki G&uuml;lc&uuml;

## Field: `main.java.org.slf4j.impl.StaticMDCBinder` / `public static final StaticMDCBinder SINGLETON`

        
        The unique instance of this class.

## Method: `main.java.org.slf4j.impl.StaticMDCBinder` / `public static final StaticMDCBinder getSingleton()`

        
        Return the singleton of this class.
        
        @return the StaticMDCBinder singleton
        @since 1.7.14

## Method: `main.java.org.slf4j.impl.StaticMDCBinder` / `public MDCAdapter getMDCA()`

        
        Currently this method always returns an instance of
        {@link StaticMDCBinder}.

# File: `main.java.org.slf4j.impl.StaticMarkerBinder`

## Package: `main.java.org.slf4j.impl.StaticMarkerBinder` / `package org.slf4j.impl`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `main.java.org.slf4j.impl.StaticMarkerBinder` / `public class StaticMarkerBinder implements MarkerFactoryBinder`

        
        
        The binding of {@link MarkerFactory} class with an actual instance of
        {@link IMarkerFactory} is performed using information returned by this class.
        
        This class is meant to provide a *dummy* StaticMarkerBinder to the slf4j-api module.
        Real implementations are found in  each SLF4J binding project, e.g. slf4j-nop,
        slf4j-simple, slf4j-log4j12 etc.
        
        @author Ceki G&uuml;lc&uuml;

## Field: `main.java.org.slf4j.impl.StaticMarkerBinder` / `public static final StaticMarkerBinder SINGLETON`

        
        The unique instance of this class.

## Method: `main.java.org.slf4j.impl.StaticMarkerBinder` / `public static StaticMarkerBinder getSingleton()`

        
        Return the singleton of this class.
        
        @return the StaticMarkerBinder singleton
        @since 1.7.14

## Method: `main.java.org.slf4j.impl.StaticMarkerBinder` / `public IMarkerFactory getMarkerFactory()`

        
        Currently this method always returns an instance of
        {@link BasicMarkerFactory}.

## Method: `main.java.org.slf4j.impl.StaticMarkerBinder` / `public String getMarkerFactoryClassStr()`

        
        Currently, this method returns the class name of
        {@link BasicMarkerFactory}.

# File: `main.java.org.slf4j.spi.LocationAwareLogger`

## Package: `main.java.org.slf4j.spi.LocationAwareLogger` / `package org.slf4j.spi`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.spi.LocationAwareLogger` / `public interface LocationAwareLogger extends Logger`

        
        An <b>optional</b> interface helping integration with logging systems capable of
        extracting location information. This interface is mainly used by SLF4J bridges
        such as jcl-over-slf4j, jul-to-slf4j and log4j-over-slf4j or {@link Logger} wrappers
        which need to provide hints so that the underlying logging system can extract
        the correct location information (method name, line number).
        
        @author Ceki Gulcu
        @since 1.3

## Method: `main.java.org.slf4j.spi.LocationAwareLogger` / `public void log(Marker marker, String fqcn, int level, String message, Object[] argArray, Throwable t)`

        
        Printing method with support for location information.
        
        @param marker The marker to be used for this event, may be null.
        @param fqcn The fully qualified class name of the <b>logger instance</b>,
        typically the logger class, logger bridge or a logger wrapper.
        @param level One of the level integers defined in this interface
        @param message The message for the log event
        @param t Throwable associated with the log event, may be null.

# File: `main.java.org.slf4j.spi.LoggerFactoryBinder`

## Package: `main.java.org.slf4j.spi.LoggerFactoryBinder` / `package org.slf4j.spi`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.spi.LoggerFactoryBinder` / `public interface LoggerFactoryBinder`

        
        An internal interface which helps the static {@link org.slf4j.LoggerFactory}
        class bind with the appropriate {@link ILoggerFactory} instance.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `main.java.org.slf4j.spi.LoggerFactoryBinder` / `public ILoggerFactory getLoggerFactory()`

        
        Return the instance of {@link ILoggerFactory} that
        {@link org.slf4j.LoggerFactory} class should bind to.
        
        @return the instance of {@link ILoggerFactory} that
        {@link org.slf4j.LoggerFactory} class should bind to.

## Method: `main.java.org.slf4j.spi.LoggerFactoryBinder` / `public String getLoggerFactoryClassStr()`

        
        The String form of the {@link ILoggerFactory} object that this
        <code>LoggerFactoryBinder</code> instance is <em>intended</em> to return.
        
        <p>This method allows the developer to intterogate this binder's intention
        which may be different from the {@link ILoggerFactory} instance it is able to
        yield in practice. The discrepency should only occur in case of errors.
        
        @return the class name of the intended {@link ILoggerFactory} instance

# File: `main.java.org.slf4j.spi.MDCAdapter`

## Package: `main.java.org.slf4j.spi.MDCAdapter` / `package org.slf4j.spi`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.spi.MDCAdapter` / `public interface MDCAdapter`

        
        This interface abstracts the service offered by various MDC
        implementations.
        
        @author Ceki G&uuml;lc&uuml;
        @since 1.4.1

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public void put(String key, String val)`

        
        Put a context value (the <code>val</code> parameter) as identified with
        the <code>key</code> parameter into the current thread's context map.
        The <code>key</code> parameter cannot be null. The code>val</code> parameter
        can be null only if the underlying implementation supports it.
        
        <p>If the current thread does not have a context map it is created as a side
        effect of this call.

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public String get(String key)`

        
        Get the context identified by the <code>key</code> parameter.
        The <code>key</code> parameter cannot be null.
        
        @return the string value identified by the <code>key</code> parameter.

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public void remove(String key)`

        
        Remove the the context identified by the <code>key</code> parameter.
        The <code>key</code> parameter cannot be null.
        
        <p>
        This method does nothing if there is no previous value
        associated with <code>key</code>.

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public void clear()`

        
        Clear all entries in the MDC.

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public Map<String, String> getCopyOfContextMap()`

        
        Return a copy of the current thread's context map, with keys and
        values of type String. Returned value may be null.
        
        @return A copy of the current thread's context map. May be null.
        @since 1.5.1

## Method: `main.java.org.slf4j.spi.MDCAdapter` / `public void setContextMap(Map<String, String> contextMap)`

        
        Set the current thread's context map by first clearing any existing
        map and then copying the map passed as parameter. The context map
        parameter must only contain keys and values of type String.
        
        @param contextMap must contain only keys and values of type String
        
        @since 1.5.1

# File: `main.java.org.slf4j.spi.MarkerFactoryBinder`

## Package: `main.java.org.slf4j.spi.MarkerFactoryBinder` / `package org.slf4j.spi`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Interface: `main.java.org.slf4j.spi.MarkerFactoryBinder` / `public interface MarkerFactoryBinder`

        
        An internal interface which helps the static {@link org.slf4j.MarkerFactory}
        class bind with the appropriate {@link IMarkerFactory} instance.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `main.java.org.slf4j.spi.MarkerFactoryBinder` / `public IMarkerFactory getMarkerFactory()`

        
        Return the instance of {@link IMarkerFactory} that
        {@link org.slf4j.MarkerFactory} class should bind to.
        
        @return the instance of {@link IMarkerFactory} that
        {@link org.slf4j.MarkerFactory} class should bind to.

## Method: `main.java.org.slf4j.spi.MarkerFactoryBinder` / `public String getMarkerFactoryClassStr()`

        
        The String form of the {@link IMarkerFactory} object that this
        <code>MarkerFactoryBinder</code> instance is <em>intended</em> to return.
        
        <p>This method allows the developer to intterogate this binder's intention
        which may be different from the {@link IMarkerFactory} instance it is able to
        return. Such a discrepency should only occur in case of errors.
        
        @return the class name of the intended {@link IMarkerFactory} instance

# File: `test.java.org.slf4j.BasicMarkerTest`

## Package: `test.java.org.slf4j.BasicMarkerTest` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.BasicMarkerTest` / `public class BasicMarkerTest`

        
        Unit test BasicMarker
        
        @author Ceki G&uuml;lc&uuml;
        @author Joern Huxhorn

# File: `test.java.org.slf4j.Differentiator`

## Package: `test.java.org.slf4j.Differentiator` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: `test.java.org.slf4j.DoubleCheckedInt`

## Class: `test.java.org.slf4j.DoubleCheckedInt` / `public class DoubleCheckedInt`

        
        This class demonstrates that threads accessing the STATE variable always see a consistent value.
        
        During ongoing initialization the observed value is either ONGOING_INITIALIZATION
        or one of {SUCCESS, FAILURE}.
        
        Post initialization the observed value is always one of  {SUCCESS, FAILURE}.
        
        See also http://jira.qos.ch/browse/SLF4J-167
        
        @author ceki

# File: `test.java.org.slf4j.LoggerAccessingThread`

## Package: `test.java.org.slf4j.LoggerAccessingThread` / `package org.slf4j`

        
        Copyright (c) 2004-2016 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: `test.java.org.slf4j.NoBindingTest`

## Package: `test.java.org.slf4j.NoBindingTest` / `package org.slf4j`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: `test.java.org.slf4j.helpers.BasicMDCAdapterTest`

## Package: `test.java.org.slf4j.helpers.BasicMDCAdapterTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2013 QOS.ch, Copyright (C) 2015 Google Inc.
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.BasicMDCAdapterTest` / `public class BasicMDCAdapterTest`

        
        Tests for {@link BasicMDCAdapter}
        
        @author Lukasz Cwik

## Class: `test.java.org.slf4j.helpers.BasicMDCAdapterTest` / `private static class RecordingExceptionHandler implements UncaughtExceptionHandler`

        A {@link UncaughtExceptionHandler} that records whether the thread threw an exception.

# File: `test.java.org.slf4j.helpers.BogoPerf`

## Package: `test.java.org.slf4j.helpers.BogoPerf` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.BogoPerf` / `public class BogoPerf`

        
        BogoPerf is used to check that the time required to perform a certain
        operation does not deteriorate over time. BogoPerf adjusts to the CPU speed
        and capabilities of the host.
        
        @author Ceki G&uuml;lc&uuml;

## Method: `test.java.org.slf4j.helpers.BogoPerf` / `private static double computeBogoIPS(int N)`

        
        Compute bogoInstructions per second
        <p>
        on a 3.2 Ghz Pentium D CPU (around 2007), we obtain about 9'000 bogoIPS.
        
        @param N
        number of bogoInstructions to average over in order to
        compute the result
        @return bogo Instructions Per Second

## Method: `test.java.org.slf4j.helpers.BogoPerf` / `public static double currentBIPS()`

        
        Computed the BogoIPS for this host CPU.
        
        @return

## Method: `test.java.org.slf4j.helpers.BogoPerf` / `public static void assertDuration(double currentDuration, long referenceDuration, double referenceBIPS) throws AssertionFailedError`

        
        Assertion used for values that <b>decrease</b> with faster CPUs, typically
        the time (duration) needed to perform a task.
        
        @param currentDuration
        @param referenceDuration
        @param referenceBIPS
        @throws AssertionFailedError

## Method: `test.java.org.slf4j.helpers.BogoPerf` / `public static void assertPerformance(double currentPerformance, long referencePerformance, double referenceBIPS) throws AssertionFailedError`

        
        Assertion used for values that <b>increase<b> with faster CPUs, typically
        the number of operations accomplished per unit of time.
        
        @param currentPerformance
        @param referencePerformance
        @param referenceBIPS
        @throws AssertionFailedError

# File: `test.java.org.slf4j.helpers.BubbleSort`

## Package: `test.java.org.slf4j.helpers.BubbleSort` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.BubbleSort` / `class BubbleSort`

        
        This class is used internally by BogoPerf, hence the package private
        (default) access.
        
        @author Ceki

# File: `test.java.org.slf4j.helpers.BubbleSortTest`

## Package: `test.java.org.slf4j.helpers.BubbleSortTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.BubbleSortTest` / `public class BubbleSortTest`

        
        Test that our BubbleSort algorithm is correctly implemented.
        
        @author Ceki

# File: `test.java.org.slf4j.helpers.MessageFormatterPerfTest`

## Package: `test.java.org.slf4j.helpers.MessageFormatterPerfTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: `test.java.org.slf4j.helpers.MessageFormatterTest`

## Package: `test.java.org.slf4j.helpers.MessageFormatterTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.MessageFormatterTest` / `public class MessageFormatterTest`

        
        @author Ceki Gulcu

# File: `test.java.org.slf4j.helpers.MyRandom`

## Package: `test.java.org.slf4j.helpers.MyRandom` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# File: `test.java.org.slf4j.helpers.SubstitutableLoggerTest`

## Package: `test.java.org.slf4j.helpers.SubstitutableLoggerTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Class: `test.java.org.slf4j.helpers.SubstitutableLoggerTest` / `public class SubstitutableLoggerTest`

        
        @author Chetan Mehrotra

# File: `test.java.org.slf4j.helpers.SubstituteLoggerFactoryTest`

## Package: `test.java.org.slf4j.helpers.SubstituteLoggerFactoryTest` / `package org.slf4j.helpers`

        
        Copyright (c) 2004-2011 QOS.ch
        All rights reserved.
        
        Permission is hereby granted, free  of charge, to any person obtaining
        a  copy  of this  software  and  associated  documentation files  (the
        "Software"), to  deal in  the Software without  restriction, including
        without limitation  the rights to  use, copy, modify,  merge, publish,
        distribute,  sublicense, and/or sell  copies of  the Software,  and to
        permit persons to whom the Software  is furnished to do so, subject to
        the following conditions:
        
        The  above  copyright  notice  and  this permission  notice  shall  be
        included in all copies or substantial portions of the Software.
        
        THE  SOFTWARE IS  PROVIDED  "AS  IS", WITHOUT  WARRANTY  OF ANY  KIND,
        EXPRESS OR  IMPLIED, INCLUDING  BUT NOT LIMITED  TO THE  WARRANTIES OF
        MERCHANTABILITY,    FITNESS    FOR    A   PARTICULAR    PURPOSE    AND
        NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
        LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
        OF CONTRACT, TORT OR OTHERWISE,  ARISING FROM, OUT OF OR IN CONNECTION
        WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

