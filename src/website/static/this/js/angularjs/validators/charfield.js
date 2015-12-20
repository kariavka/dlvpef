/* CharField.
 * Any text field which may have a limitations on the length of the content.
 * Usage:
 *     $scope.user = {
 *         firstname: new CharField({min_length:3, max_length:20});
 *         secondname: new CharField({min_length:3, max_length:20});
 *         about: new CharField({min_length:0, max_length:0, required:false});
 *     };
 *
 * Prototype:
 *     function CharField(_options)
 *
 *     The ``_options`` variable can accept the following values:
 *         * init:string - initialization string (default:null), example:
 *             $scope.fullname = new CharField({init:"Jon Smit"});
 *         or
 *             $scope.fullname = new CharField();
 *             $scope.fullname.model = "Jon Smit";
 *
 *         * min_length:int - the minimum length of the string (default:3).
 *             If set to ``0`` - the minimum value will be ignored.
 *
 *         * max_length:int - the maximum length of the string (default:32).
 *             If set to ``0`` - the maximum value will bw ignored.
 *
 *         * required:bool - determines whether the field is required
 *             (default:true).
 *
 *         * regex:regexp - regular expression to validate the contents
 *             (defaults:[.\n\r\b]*).
 *
 *         P.s. Other parameters will be ignored.
 *
 * Option's methods:
 *     * obj.getOptions() - return current object's options.
 *     * obj.setOptions(_options) - set new options.
 *
 * Methods:
 *     * isRequired() - return ``true`` if the field is required.
 */
var CharFieldNamespace = (function() {
    var CharField = function(_options) {
        // Constructor of CharField.
        // Options by defaults.
        var options = {
            init: null,
            min_length: 0,
            max_length: 0,
            required: false,
            regex: /[.\n\r\b]*/,
            init_default_key: 'default',
        };

        this.getOptions = function() {
            // Return options.
            return options;
        } // end getOptions().

        this.setOptions = function(_options) {
            // Set new options (update options).
            if (_options)
                for (var opt in _options)
                    if (opt in options)
                        options[opt] = _options[opt];

            if (_options && "init" in _options)
                if (_options.init !== options.init_default_key)
                    this.model = _options.init
        } // end setOptions();

        this.model = null;
        this.setOptions(_options);
    } // end CharField().


    CharField.prototype.isRequired = function() {
        // Return ``true`` if field is required.
        return this.getOptions().required;
    } // end isRequired().


    CharField.prototype.isValid = function() {
        // Return ``true`` if value of field is valid.
        var options = this.getOptions();

        if (this.model === null)
            return false;

        if (this.isShortError())
            return false;

        if (this.isLongError())
            return false;

        if (this.isCorrectError())
            return false;

        return true;
    } // end isValid().


    CharField.prototype.getValue = function() {
        // Return value if it is valid or empty string.
        return this.isValid() ? this.model : "";
    } // end getValue().


    CharField.prototype.isShortError = function() {
        // Return ``true`` if text in model is short.
        var options = this.getOptions();

        if (this.model === null)
            return false;

        if (options.min_length > 0 && this.model.length < options.min_length)
            return true;

        return false;
    } // end isShortStringError().


    CharField.prototype.isLongError = function() {
        // Return ``true`` if text in model is long.
        var options = this.getOptions();

        if (this.model === null)
            return false;

        if (options.max_length > 0 && this.model.length > options.max_length)
            return true;

        return false;
    } // end isShortStringError().


    CharField.prototype.isCorrectError = function() {
        // Return ``true`` if text is correct.
        var options = this.getOptions();

        if (this.model === null)
            return false;

        if (!options.regex.test(this.model))
            return true;

        return false;
    } // end isCorrectError().


    CharField.prototype.isRequiredError = function(_dirty) {
        // Return ``true`` if field is empty but it is required.
        var dirty = _dirty !== undefined ? _dirty : true,
            is_dirty = this.model !== null;

        if (dirty) {
            if (this.isRequired() && is_dirty && !this.model)
                return true;
        } else {
            if (this.isRequired() && !this.model)
                return true;
        }

        return false;
    } // end isRequiredError().


    CharField.prototype.isClean = function() {
        // Returns ``true`` if the field is filled out correctly.
        if (this.isShortError() || this.isLongError() ||
            this.isCorrectError() || this.isRequiredError(false))
                return false;

        return true;
    } // end isClean().


    CharField.prototype.isValidError = function() {
        // Return true if the email is invalid.
        return this.model ? !this.isClean() : false;
    } // end isValidError().

    return {
        CharField: CharField,
    }
}()); // end CharFieldNamespace().


// CharField.
var CharField = CharFieldNamespace.CharField;

