/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const toBe = (expectedVal) => {
        if (val === expectedVal) return true;
        throw new Error("Not Equal");
    }

    const notToBe = (expectedVal) => {
        if (val !== expectedVal) return true;
        throw new Error("Equal");
    }

    return { toBe, notToBe }
};