using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using idpSpin.Models;

namespace idpSpin.Controllers
{
    public class SpinController : Controller
    {
        private readonly SpinContext _context;

        public SpinController(SpinContext context)
        {
            _context = context;    
        }

        // GET: Spin
        public async Task<IActionResult> Index()
        {
            return View(await _context.Spin.ToListAsync());
        }

        // GET: Spin/Details/5
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var spin = await _context.Spin
                .SingleOrDefaultAsync(m => m.Id == id);
            if (spin == null)
            {
                return NotFound();
            }

            return View(spin);
        }

        // GET: Spin/Create
        public IActionResult Create()
        {
            return View();
        }

        // POST: Spin/Create
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Servo1,Servo2,Servo3,Servo4,Servo5,Servo6,Servo7,Servo8,Servo9,Servo10,Servo11,Servo12,Servo13,Servo14,Servo15,Servo16,Servo17,Servo18,HellingSensor,Tijd,GeluidSensor")] Spin spin)
        {
            if (ModelState.IsValid)
            {
                _context.Add(spin);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }
            return View(spin);
        }

        // GET: Spin/Edit/5
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var spin = await _context.Spin.SingleOrDefaultAsync(m => m.Id == id);
            if (spin == null)
            {
                return NotFound();
            }
            return View(spin);
        }

        // POST: Spin/Edit/5
        // To protect from overposting attacks, please enable the specific properties you want to bind to, for 
        // more details see http://go.microsoft.com/fwlink/?LinkId=317598.
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Servo1,Servo2,Servo3,Servo4,Servo5,Servo6,Servo7,Servo8,Servo9,Servo10,Servo11,Servo12,Servo13,Servo14,Servo15,Servo16,Servo17,Servo18,HellingSensor,Tijd,GeluidSensor")] Spin spin)
        {
            if (id != spin.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(spin);
                    await _context.SaveChangesAsync();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!SpinExists(spin.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction("Index");
            }
            return View(spin);
        }

        // GET: Spin/Delete/5
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var spin = await _context.Spin
                .SingleOrDefaultAsync(m => m.Id == id);
            if (spin == null)
            {
                return NotFound();
            }

            return View(spin);
        }

        // POST: Spin/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var spin = await _context.Spin.SingleOrDefaultAsync(m => m.Id == id);
            _context.Spin.Remove(spin);
            await _context.SaveChangesAsync();
            return RedirectToAction("Index");
        }

        private bool SpinExists(int id)
        {
            return _context.Spin.Any(e => e.Id == id);
        }
    }
}
