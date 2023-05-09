From: <Saved by Blink>
Snapshot-Content-Location: https://greasyfork.org/scripts/17665-openload/code/openload.user.js
Subject: 
Date: Tue, 7 Mar 2023 11:44:43 -0000
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--kOI8HnuGFpV5YNXO0WScRdSOTcZsyBGRVZR2tSqQhJ----"


------MultipartBoundary--kOI8HnuGFpV5YNXO0WScRdSOTcZsyBGRVZR2tSqQhJ----
Content-Type: text/html
Content-ID: <frame-EE3023CA10EC13CE97C6D62640F085AF@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://greasyfork.org/scripts/17665-openload/code/openload.user.js

<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=
=3DUTF-8"><link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-38e8cc=
ec-ff80-41d0-a5da-84bbde9aec03@mhtml.blink" /></head><body><pre style=3D"wo=
rd-wrap: break-word; white-space: pre-wrap;">// =3D=3DUserScript=3D=3D
// @author       @leoncastro
// @namespace    https://github.com/leoncastro
// @name         openload
// @version      0.14.8
// @description  Remove anti-adblock, ads, popups and timer waits, and show=
 direct download link
// @icon         data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMA=
AABEpIrGAAAA/FBMVEUAAAAeP2MAmNkAoN8hNlgSSWwXLUgEITELKT8OMEkAn94Ant4AmtsAldQ=
BW4MFh8YAktQBicxjT5sAnt4AX4lEcbUTeLBgVqBcXKMAnNxMS4pKbbEuQGwAmtoAY44xebwAk9=
QGjM1jT5tcTZUPM01jT5s7OGZfWKEAaJUAod8Ak9VYYqhSZKgVg8Ujf8AKSm4Agr5mPZRmPZRmP=
ZRlR5gAod8AldNXXKEAltQAjMcAmNVWZKpeWaJUZqtKbbE+dbg+dLdEcLM7d7omgMExersAk9Rg=
VqA7aKUAod8Ak9UAn99lR5gAm9wJhshRaa0ue74mgMEAjdBmPZQ7d7qePASIAAAASHRSTlMAOP7=
5GiksAgcPxb3QS0Nh0+T+0hj+Yv796m3PSLNc0eF0vYgg7l/DOPDs/ejo11dV+LpM8et8qaduic=
HV0L7Jrer75omU6GL8xLQIAAABaklEQVR42u1S2XaCMBQMaxJAAcUFRcG673Zzb9VWW4Pi0v7/v=
zSCcDz9hfY+3pnMmZkb8IcG8YIoVNDtQhRFPlyg+LQgy3JhE4fBAjLr5evrbFS2fAqeJDl3v9+z=
rDbwGShtv6VSh0M7O89hipearsuZTotliaMiAFH6/fidWnU67WymShmx5pZLpjHAaY2QggiQ2j0=
dbQrg3DyTeHoE8nYrNXzpuOZseKjq3sm2Aiv1xO4BcNvnIrp66wtwoHtez4KB+1p1dw+oABPFgw=
ON4v0wn3i3+6KEQiXCY9rZ0yMcVAKCJIaFUPysFxGGNwqBh/A9Oeuqoa6ZWw80hRykoDjRSzDeP=
dnMTQragysVDWSoCiGtEr4QjotPHvG1ut8DnnKuayYVxWRJa4ghrZY2ucrnXzrZTKKMAcRD0w1u=
4UwQBJeue9dbfJR56F9zLCmKIo0bYTxmuaAKs5GFwvyGIAgG/PVB6Ov/ieYHpLEydStkqm4AAAA=
ASUVORK5CYII=3D
// @include      http://openload.co
// @include      /^(https?:)?\/\/(openload\.(co|pw)|oload\.(\w+)|oladblock\=
.(me|services|xyz))\/*.*/
// @compatible   firefox+greasemonkey(3.17)
// @compatible   firefox+tampermonkey
// @compatible   chrome+tampermonkey
// @grant        none
// @run-at       document-start
// =3D=3D/UserScript=3D=3D
(function(){
 //
 // @run-at document-start
 //
 window.adblock=3Dfalse;
 window.adblock2=3Dfalse;
 window.turnoff=3Dtrue;
 window.open=3Dfunction(){};
 //
 // @run-at document-end
 //
 function onready(fn){if(document.readyState!=3D'loading')fn();else documen=
t.addEventListener('DOMContentLoaded',fn);}

 onready(function(){
  if( document.location.href.match(/\/embed\//) || $('#realdl&gt;a') )
  {
   $('#btnView').hide();
   $('#btnDl').hide();
   $('.dlButtonContainer').show();
   $('h3.dlfile.h-method').hide();
   $('.col-md-4.col-centered-sm *').remove();
   $('#mgiframe,#main&gt;div[id]').remove();
   $('#downloadTimer').hide();
   $('#mediaspace_wrapper').prepend( $('&lt;div/&gt;').attr('id', 'realdl')
    .attr('style', 'position: absolute; top: 0 ; left: 0 ; right: 0; text-a=
lign: center; z-index: 9999; background-color: #000; padding: .5em 0;')
    .on('mouseenter', function(){ $(this).fadeTo(500, 1); }).on('mouseleave=
', function(){ $(this).fadeTo(500, 0); })
    .append( $('&lt;a/&gt;').attr('href', '').attr('style', 'color: #fff; t=
ext-decoration: none; -moz-user-select: none;').text('DOWNLOAD') )
    .append( $('&lt;span/&gt;').attr('style', 'color: #fff; padding-left: 1=
em;').attr('id', 'steamcopy') ) );
   $('#realdl').show();
   var streamurl_tmr =3D setInterval(function(){
    // &lt;@snippet edited author=3D"https://greasyfork.org/forum/profile/d=
aedelus" src=3D"https://greasyfork.org/forum/discussion/36362/x"&gt;
    var streamurl_src;
    var streamurl_end =3D false;
    $('p[id]').each(function(){
     if( !streamurl_end )
     {
      streamurl_src =3D streamurl_src || ($(this).text().match(/^[\w\.~-]+$=
/) /*TEMP_FIX: &amp;&amp; $(this).text().match(/~/) */) ? $(this).text() : =
streamurl_src;
      if( streamurl_src )
       streamurl_end =3D true;
     }
    });
    // &lt;/@snippet&gt;
    if( streamurl_src )
    {
     var streamurl_url =3D location.origin + '/stream/' + /*TEMP_FIX: strea=
murl_src + */$('#DtsBlkVFQx').text();
     $('#realdl a').attr('href', streamurl_url);
     $('#steamcopy').text( streamurl_url );
     $('#videooverlay').click();
     $('div[style]').each(function(){ if(this.style.zIndex&amp;&amp;this.id=
!=3D'realdl') this.remove(); });
     clearInterval(streamurl_tmr);
    }
   },100);
  }
  window.onclick=3Dfunction(){};
  document.onclick=3Dfunction(){};
  document.body.onclick=3Dfunction(){};
 });

})();</pre></body></html>
------MultipartBoundary--kOI8HnuGFpV5YNXO0WScRdSOTcZsyBGRVZR2tSqQhJ----
Content-Type: text/css
Content-Transfer-Encoding: quoted-printable
Content-Location: cid:css-38e8ccec-ff80-41d0-a5da-84bbde9aec03@mhtml.blink

@charset "utf-8";
=0A
------MultipartBoundary--kOI8HnuGFpV5YNXO0WScRdSOTcZsyBGRVZR2tSqQhJ------
