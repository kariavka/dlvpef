/* Initialize an AngularJS application.
 *
 * Just upload this module to your page with AngularJS. Definition the name of
 * AngularJs application and it initialization will be executed by automatic.
 *
 * You can configure `_APPLICATION_NAME_BY_DEFAULTS` variable for fast
 * initialization of AngularJs. Just enter the name of AngularJS application.
 *
 */
_APPLICATION_NAME_BY_DEFAULTS = null;


/* Special functions section.
 *
 * The functions of quick search for an element by attribute and and specify
 * the name of the AngularJS application.
 *
 */
function getElementsByAttribute(tagName, attrName, onlyFirst) {
    // Return the list of elements of specific tag that has the specified attr.
    // Examples:
    //      getElementsByAttribute("div", "data-custom-size");
    //
    // If the name of tag is unknown - you can use `*` symbol as `tagNmae`
    // parameter for search by all tags.
    // Examples:
    //      getElementsByAttribute("*", "data-custom-size");
    //
    // You can get only the first element - use `onlyFirst` as` true`.
    // Examples:
    //      getElementsByAttribute("div", "data-custom-size", true);
    //      getElementsByAttribute("*", "data-custom-size", true);
    //
    var resultElements = new Array(),
        foundElements = document.getElementsByTagName(tagName),
        onlyFirst = typeof onlyFirst !== "undefined" ? onlyFirst : false;

    for (var i=0; i<foundElements.length; i++) {
        var currentElement = foundElements[i];
        if (currentElement.getAttribute(attrName) !== null) {
            resultElements.push(currentElement);
            if (onlyFirst) break;
        }
    } // end for ().

    return resultElements;
} // end getElementsByAttribute().


function getAngularJsAppName(defaults) {
    // Returns the name of AngularJs application.
    // The function tries to determine the name of the application by searching
    // for `ng-app` attribute. If an element with the specified attribute is
    // not found - used the default value.
    var defaults = typeof defaults !== "undefined" ? defaults : "ngApp",
        elements = getElementsByAttribute("*", "ng-app", true);

    if (elements.length < 1)
        return defaults;

    return elements[0].getAttribute("ng-app");
} // end getAngularJsAppName().


/* Activate of AngularJS.
 *
 * For compatibility with Django, Jinja and Tornado templates, set the
 * following processing units: {$ expression $}.
 *
 */
var _APPLICATION_NAME = _APPLICATION_NAME_BY_DEFAULTS || getAngularJsAppName(),
    app = angular.module(_APPLICATION_NAME, []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol("{$");
    $interpolateProvider.endSymbol("$}");
});

